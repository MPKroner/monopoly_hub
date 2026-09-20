const CACHE_NAME = "monopoly-hub-v1";
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
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(ASSETS_TO_CACHE).catch(function(err) {
        console.warn("Precache failed for some assets, continuing:", err);
      });
    }).then(function() {
      return self.skipWaiting();
    })
  );
});

// Activate Event: Clean old caches
self.addEventListener("activate", function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(name) {
          if (name !== CACHE_NAME) {
            return caches.delete(name);
          }
        })
      );
    }).then(function() {
      return self.clients.claim();
    })
  );
});

// Fetch Event: Cache First with Dynamic Caching & Offline Fallback
self.addEventListener("fetch", function(event) {
  // Only handle GET requests and skip external APIs (Gemini, Google)
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);

  // Do not cache API calls to Google or external services
  if (url.hostname.includes("googleapis.com") || url.hostname.includes("google.com")) {
    return;
  }

  event.respondWith(
    caches.match(event.request).then(function(cachedResponse) {
      if (cachedResponse) {
        // Return from cache immediately
        return cachedResponse;
      }

      // Fetch from network and dynamically cache same-origin assets
      return fetch(event.request).then(function(networkResponse) {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== "basic") {
          return networkResponse;
        }

        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(event.request, responseToCache);
        });

        return networkResponse;
      }).catch(function() {
        // If offline and request is for HTML navigation, return index.html from cache
        if (event.request.headers.get("accept") && event.request.headers.get("accept").includes("text/html")) {
          return caches.match("./index.html");
        }
      });
    })
  );
});
