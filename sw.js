const CACHE_NAME = "monopoly-hub-v6";
const ASSETS_TO_CACHE = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/icon.svg"
];

// Install Event: Precaching core shell
self.addEventListener("install", function(event) {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(ASSETS_TO_CACHE).catch(function(err) {
        console.warn("Precache notice:", err);
      });
    })
  );
});

// Activate Event: Clean old caches immediately and claim clients
self.addEventListener("activate", function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(name) {
          if (name !== CACHE_NAME) {
            console.log("Purging old cache:", name);
            return caches.delete(name);
          }
        })
      );
    }).then(function() {
      return self.clients.claim();
    })
  );
});

// Fetch Event: Network-First for HTML (to get updates), Cache-First for static assets
self.addEventListener("fetch", function(event) {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);

  // Skip Google Gemini / external APIs & live search
  if (url.hostname.includes("googleapis.com") || url.hostname.includes("google.com") || url.hostname.includes("fandom.com") || url.hostname.includes("wikimedia.org") || url.hostname.includes("wikipedia.org")) {
    return;
  }

  // HTML Navigation: Network first, fallback to offline cache
  const isHtml = event.request.mode === "navigate" || (event.request.headers.get("accept") && event.request.headers.get("accept").includes("text/html"));
  if (isHtml) {
    event.respondWith(
      fetch(event.request).then(function(networkResponse) {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then(function(cache) {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      }).catch(function() {
        return caches.match("./index.html") || caches.match("./");
      })
    );
    return;
  }

  // Static Assets (Images, Icons, CSS, JS): Cache first, fallback to network
  event.respondWith(
    caches.match(event.request).then(function(cachedResponse) {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then(function(networkResponse) {
        if (!networkResponse || networkResponse.status !== 200) {
          return networkResponse;
        }
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      });
    })
  );
});
