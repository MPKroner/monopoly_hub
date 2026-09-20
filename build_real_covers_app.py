# -*- coding: utf-8 -*-
import json

with open("editions_seed.json", "r", encoding="utf-8") as f:
    seed_data = json.load(f)

json_str = json.dumps(seed_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Monopoly Collector Hub - Suivi de Collection avec Vraies Jaquettes</title>
  <style>
    :root {
      --bg-main: #0b0f19;
      --bg-card: #151d30;
      --bg-card-hover: #1c2742;
      --bg-surface: #151d30;
      --border-color: #24324f;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #e11d48;
      --primary-hover: #be123c;
      --accent: #38bdf8;
      --success: #10b981;
      --warning: #f59e0b;
      --tag-bg: rgba(56, 189, 248, 0.12);
      --card-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -4px rgba(0, 0, 0, 0.3);
      --box-shadow: 0 12px 20px -4px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.3);
      --radius: 12px;
      --font: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }

    [data-theme="light"] {
      --bg-main: #f1f5f9;
      --bg-card: #ffffff;
      --bg-card-hover: #f8fafc;
      --bg-surface: #ffffff;
      --border-color: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --primary: #dc2626;
      --primary-hover: #b91c1c;
      --accent: #0284c7;
      --success: #059669;
      --warning: #d97706;
      --tag-bg: rgba(2, 132, 199, 0.1);
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --box-shadow: 0 8px 16px -2px rgba(0, 0, 0, 0.12);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s, border-color 0.2s;
    }

    body {
      font-family: var(--font);
      background-color: var(--bg-main);
      color: var(--text-main);
      min-height: 100vh;
      padding-bottom: 60px;
    }

    header {
      background: linear-gradient(135deg, #9f1239 0%, #151d30 100%);
      padding: 22px 20px;
      box-shadow: 0 4px 25px rgba(0,0,0,0.35);
      border-bottom: 2px solid #e11d48;
    }

    .header-content {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .logo-area {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .logo-icon {
      width: 48px;
      height: 48px;
      background: #e11d48;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 26px;
      color: white;
      box-shadow: 0 4px 12px rgba(225, 29, 72, 0.45);
      border: 2px solid #fff;
    }

    .header-title h1 {
      font-size: 1.65rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: #fff;
    }

    .header-title p {
      font-size: 0.88rem;
      color: #fbcfe8;
      opacity: 0.9;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.86rem;
      font-weight: 600;
      cursor: pointer;
      border: none;
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-primary {
      background-color: var(--primary);
      color: white;
    }
    .btn-primary:hover {
      background-color: var(--primary-hover);
      transform: translateY(-1px);
    }

    .btn-secondary {
      background-color: var(--bg-card);
      color: var(--text-main);
      border: 1px solid var(--border-color);
    }
    .btn-secondary:hover {
      background-color: var(--bg-card-hover);
    }

    .container {
      max-width: 1440px;
      margin: 24px auto 0;
      padding: 0 20px;
    }

    /* STATS DASHBOARD */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .stat-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 18px 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 8px;
      position: relative;
      overflow: hidden;
    }

    .stat-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--accent);
    }
    .stat-card.owned::before { background: var(--success); }
    .stat-card.wishlist::before { background: var(--warning); }
    .stat-card.total::before { background: var(--primary); }
    .stat-card.value::before { background: #8b5cf6; }

    .stat-title {
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      font-weight: 600;
    }

    .stat-value {
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .stat-sub {
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    .progress-bar-container {
      width: 100%;
      height: 8px;
      background: rgba(255,255,255,0.08);
      border-radius: 4px;
      overflow: hidden;
      margin-top: 4px;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #10b981, #38bdf8);
      border-radius: 4px;
      transition: width 0.4s ease;
    }

    /* CONTROLS & FILTERS */
    .controls-panel {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .search-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }

    .search-box {
      flex: 1;
      min-width: 260px;
      position: relative;
    }

    .search-box input {
      width: 100%;
      padding: 12px 16px 12px 42px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
    }

    .search-box input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      width: 18px;
      height: 18px;
    }

    .filter-select {
      padding: 11px 14px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 0.9rem;
      cursor: pointer;
      outline: none;
    }

    .pills-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }

    .pill {
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border-color);
      background: var(--bg-main);
      color: var(--text-muted);
      transition: all 0.15s ease;
      user-select: none;
    }

    .pill:hover {
      border-color: var(--accent);
      color: var(--text-main);
    }

    .pill.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .view-toggle {
      margin-left: auto;
      display: flex;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: hidden;
    }

    .view-btn {
      padding: 8px 12px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 0.85rem;
    }

    .view-btn.active {
      background: var(--primary);
      color: white;
      font-weight: 600;
    }

    /* CARDS GRID */
    .grid-view {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
    }

    .edition-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 0;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: transform 0.22s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.22s ease, box-shadow 0.22s ease;
    }

    .edition-card:hover {
      transform: translateY(-4px);
      border-color: rgba(56, 189, 248, 0.45);
      box-shadow: 0 16px 24px -4px rgba(0, 0, 0, 0.5);
    }

    /* REAL BOX COVER CONTAINER */
    .box-cover-wrapper {
      width: 100%;
      height: 200px;
      position: relative;
      cursor: pointer;
      overflow: hidden;
      background: #060911;
      border-bottom: 2px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .box-cover-image {
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #070c18;
      padding: 6px;
      transition: transform 0.3s ease;
    }

    .edition-card:hover .box-cover-image {
      transform: scale(1.05);
    }

    /* Unverified / Missing Cover Placeholder */
    .missing-cover-box {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 16px;
      text-align: center;
      gap: 8px;
      background: linear-gradient(145deg, #131b2e 0%, #0a0f1d 100%);
      color: var(--text-muted);
    }

    .missing-icon {
      font-size: 2rem;
      opacity: 0.7;
    }

    .missing-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      max-width: 90%;
    }

    .missing-sub {
      font-size: 0.75rem;
      color: #94a3b8;
    }

    /* Verified real photo badge */
    .verified-badge {
      position: absolute;
      bottom: 8px;
      left: 8px;
      background: rgba(16, 185, 129, 0.92);
      color: white;
      font-size: 0.68rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      backdrop-filter: blur(4px);
      box-shadow: 0 2px 5px rgba(0,0,0,0.4);
      z-index: 4;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .status-ribbon {
      position: absolute;
      top: 10px;
      right: 10px;
      z-index: 5;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.3px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.4);
      backdrop-filter: blur(4px);
    }
    .status-ribbon.owned {
      background: rgba(16, 185, 129, 0.95);
      color: white;
    }
    .status-ribbon.wishlist {
      background: rgba(245, 158, 11, 0.95);
      color: #0f172a;
    }
    .status-ribbon.none {
      background: rgba(15, 23, 42, 0.85);
      color: #94a3b8;
      border: 1px solid rgba(255,255,255,0.2);
    }

    /* Card Content Area */
    .card-body {
      padding: 16px 18px 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex-grow: 1;
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
    }

    .card-category {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 3px 8px;
      border-radius: 4px;
      background: var(--tag-bg);
      color: var(--accent);
      display: inline-block;
    }

    .card-year {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
    }

    .card-desc {
      font-size: 0.83rem;
      color: var(--text-muted);
      line-height: 1.45;
      flex-grow: 1;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .card-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      font-size: 0.78rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border-color);
      padding-top: 10px;
    }

    .meta-item {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .card-user-info {
      background: rgba(0,0,0,0.18);
      border-radius: 6px;
      padding: 8px 10px;
      font-size: 0.78rem;
      display: flex;
      flex-direction: column;
      gap: 4px;
      border: 1px dashed var(--border-color);
    }

    .card-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      padding-top: 6px;
      margin-top: auto;
    }

    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 20px;
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }
    .status-badge.owned {
      background: rgba(16, 185, 129, 0.18);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }
    .status-badge.wishlist {
      background: rgba(245, 158, 11, 0.18);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .status-badge.none {
      background: rgba(148, 163, 184, 0.15);
      color: var(--text-muted);
      border: 1px solid rgba(148, 163, 184, 0.3);
    }

    .btn-google {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 0.76rem;
      color: var(--accent);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 6px;
      padding: 5px 9px;
      text-decoration: none;
    }
    .btn-google:hover {
      background: rgba(56, 189, 248, 0.2);
    }

    /* TABLE VIEW */
    .table-container {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      overflow-x: auto;
      box-shadow: var(--card-shadow);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }

    th {
      background: rgba(0,0,0,0.25);
      padding: 12px 16px;
      font-weight: 700;
      color: var(--text-muted);
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }

    td {
      padding: 10px 16px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
    }

    .table-thumb {
      width: 54px;
      height: 38px;
      border-radius: 4px;
      object-fit: contain;
      background: #090d16;
      cursor: pointer;
      border: 1px solid var(--border-color);
    }

    /* MODALS */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(5px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 999;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
      padding: 16px;
    }

    .modal-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      width: 100%;
      max-width: 660px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.6);
      transform: translateY(20px);
      transition: transform 0.2s ease;
    }

    .modal-backdrop.open .modal {
      transform: translateY(0);
    }

    .modal-header {
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .modal-header h3 {
      font-size: 1.25rem;
      font-weight: 700;
    }

    .close-btn {
      background: transparent;
      border: none;
      font-size: 1.5rem;
      color: var(--text-muted);
      cursor: pointer;
      line-height: 1;
    }

    .modal-body {
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .form-group label {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .form-control {
      width: 100%;
      padding: 10px 14px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 0.9rem;
      outline: none;
    }

    .form-control:focus {
      border-color: var(--accent);
    }

    .form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    .modal-footer {
      padding: 16px 24px;
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: flex-end;
      gap: 10px;
    }

    .modal-image-preview-area {
      display: flex;
      gap: 16px;
      align-items: center;
      background: rgba(0,0,0,0.25);
      padding: 14px;
      border-radius: 8px;
      border: 1px dashed var(--border-color);
    }

    .preview-box-thumb {
      width: 110px;
      height: 75px;
      border-radius: 6px;
      object-fit: contain;
      background: #090d16;
      border: 1px solid var(--border-color);
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .image-inputs-col {
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }

    /* LIGHTBOX FOR FULL VIEW */
    .lightbox-modal {
      max-width: 780px;
      text-align: center;
    }

    .lightbox-img {
      max-width: 100%;
      max-height: 60vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: var(--box-shadow);
      margin-bottom: 16px;
      background: #090d16;
      padding: 8px;
    }

    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: white;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 600;
      box-shadow: 0 4px 14px rgba(0,0,0,0.35);
      z-index: 1000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s ease;
    }
    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    .empty-state {
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
    }

    @media (max-width: 768px) {
      .form-row { grid-template-columns: 1fr; }
      .search-box { min-width: 100%; }
      .modal-image-preview-area { flex-direction: column; align-items: stretch; }
      .preview-box-thumb { width: 100%; height: 140px; }
    }
  </style>
</head>
<body data-theme="dark">

  <header>
    <div class="header-content">
      <div class="logo-area">
        <div class="logo-icon">M</div>
        <div class="header-title">
          <h1>Monopoly Collector Hub</h1>
          <p>Inventaire avec vraies jaquettes physiques et photographies officielles</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="btn btn-secondary" id="themeBtn" title="Basculer thème clair/sombre">🌓 Thème</button>
        <button class="btn btn-secondary" id="exportCsvBtn" title="Exporter pour Excel">📊 Export Excel/CSV</button>
        <button class="btn btn-secondary" id="backupJsonBtn" title="Sauvegarder les données">💾 Sauvegarder (JSON)</button>
        <label class="btn btn-secondary" style="cursor:pointer;" title="Restaurer une sauvegarde">
          📂 Importer
          <input type="file" id="importJsonInput" accept=".json" style="display: none;">
        </label>
        <button class="btn btn-primary" id="addCustomBtn">➕ Ajouter une édition</button>
      </div>
    </div>
  </header>

  <div class="container">

    <!-- STATS OVERVIEW -->
    <div class="stats-grid">
      <div class="stat-card total">
        <div class="stat-title">Éditions Répertoriées</div>
        <div class="stat-value" id="statTotal">0</div>
        <div class="stat-sub"><span id="statWithPhotos">0</span> avec vraies photos de boîte</div>
      </div>
      <div class="stat-card owned">
        <div class="stat-title">Éditions Possédées</div>
        <div class="stat-value">
          <span id="statOwned">0</span>
          <span style="font-size: 1rem; font-weight: normal; color: var(--success);" id="statOwnedPct">(0%)</span>
        </div>
        <div class="progress-bar-container">
          <div class="progress-bar-fill" id="statProgressBar" style="width: 0%;"></div>
        </div>
      </div>
      <div class="stat-card wishlist">
        <div class="stat-title">Recherchées (Wishlist)</div>
        <div class="stat-value" id="statWishlist">0</div>
        <div class="stat-sub">À acquérir prochainement</div>
      </div>
      <div class="stat-card value">
        <div class="stat-title">Valeur Estimée Collection</div>
        <div class="stat-value" id="statEstimatedValue">0 €</div>
        <div class="stat-sub">Investi : <span id="statSpentValue">0 €</span></div>
      </div>
    </div>

    <!-- CONTROLS & FILTERS -->
    <div class="controls-panel">
      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" id="searchInput" placeholder="Rechercher une édition, ville, licence, pion, pays...">
        </div>

        <select id="countrySelect" class="filter-select">
          <option value="all">Tous les Pays / Régions</option>
        </select>

        <select id="sortSelect" class="filter-select">
          <option value="name-asc">Nom (A → Z)</option>
          <option value="name-desc">Nom (Z → A)</option>
          <option value="year-desc">Année (Plus récente)</option>
          <option value="year-asc">Année (Plus ancienne)</option>
          <option value="status">Statut (Possédé en premier)</option>
        </select>

        <div class="view-toggle">
          <button class="view-btn active" id="cardViewBtn" title="Vue Boîtes & Cartes">🗂️ Jaquettes</button>
          <button class="view-btn" id="tableViewBtn" title="Vue Tableau">📋 Liste</button>
        </div>
      </div>

      <!-- STATUS & CATEGORY PILLS -->
      <div class="pills-row" id="statusPills">
        <span class="pill active" data-status="all">Tous (<span id="countAll">0</span>)</span>
        <span class="pill" data-status="owned">🟢 Possédés (<span id="countOwned">0</span>)</span>
        <span class="pill" data-status="wishlist">⭐ Recherchés (<span id="countWishlist">0</span>)</span>
        <span class="pill" data-status="none">⚪ Non possédés (<span id="countNone">0</span>)</span>
      </div>

      <div class="pills-row" id="categoryPills">
        <span class="pill active" data-category="all">Toutes les catégories</span>
      </div>
    </div>

    <!-- LISTING AREA -->
    <div id="cardsContainer" class="grid-view"></div>
    <div id="tableContainer" class="table-container" style="display: none;">
      <table>
        <thead>
          <tr>
            <th>Jaquette</th>
            <th>Statut</th>
            <th>Nom de l'Édition</th>
            <th>Catégorie</th>
            <th>Année</th>
            <th>Pays / Langue</th>
            <th>État</th>
            <th>Prix</th>
            <th>Valeur</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>

    <div id="emptyState" class="empty-state" style="display: none;">
      <h3>Aucune édition ne correspond à vos filtres</h3>
      <p style="margin-top: 6px;">Essayez d'ajuster votre recherche ou réinitialisez les filtres.</p>
    </div>

  </div>

  <!-- MODAL: EDIT USER DETAILS & PHOTO -->
  <div class="modal-backdrop" id="editModalBackdrop">
    <div class="modal">
      <div class="modal-header">
        <h3 id="editModalTitle">Détails de l'édition</h3>
        <button class="close-btn" id="closeEditModal">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="editItemId">

        <!-- Image Management -->
        <div class="form-group">
          <label>Photo Réelle de la Boîte</label>
          <div class="modal-image-preview-area">
            <div id="modalImagePreviewContainer" class="preview-box-thumb"></div>
            <div class="image-inputs-col">
              <input type="text" id="editImageUrl" class="form-control" placeholder="Coller l'URL d'une photo en ligne...">
              <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
                <label class="btn btn-secondary" style="font-size: 0.8rem; padding: 6px 12px; cursor: pointer;">
                  📸 Charger la photo de ma boîte
                  <input type="file" id="editImageFileInput" accept="image/*" style="display: none;">
                </label>
                <a id="modalGoogleSearchBtn" class="btn-google" target="_blank" href="#" title="Chercher des photos sur Google Images">
                  🔍 Trouver sur Google Images
                </a>
                <button type="button" class="btn btn-secondary" id="clearImageBtn" style="font-size: 0.8rem; padding: 6px 10px;">🗑️ Retirer</button>
              </div>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label>Statut de possession</label>
          <select id="editStatus" class="form-control">
            <option value="none">⚪ Non possédé</option>
            <option value="owned">🟢 Possédé (Dans ma collection)</option>
            <option value="wishlist">⭐ Recherché (Dans ma wishlist)</option>
          </select>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>État de la boîte / jeu</label>
            <select id="editCondition" class="form-control">
              <option value="">Non spécifié</option>
              <option value="Neuf sous blister">Neuf sous blister (Scellé)</option>
              <option value="Comme neuf">Comme neuf (Complet)</option>
              <option value="Très bon état">Très bon état</option>
              <option value="Bon état">Bon état</option>
              <option value="Usé">Usé (Boîte frottée)</option>
              <option value="Incomplet">Incomplet (Pièces manquantes)</option>
            </select>
          </div>
          <div class="form-group">
            <label>Emplacement / Rangement</label>
            <input type="text" id="editLocation" class="form-control" placeholder="Ex: Étagère A, Salon, Boîte #3...">
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Prix d'achat (€)</label>
            <input type="number" step="0.5" id="editPrice" class="form-control" placeholder="Ex: 25.00">
          </div>
          <div class="form-group">
            <label>Valeur estimée (€)</label>
            <input type="number" step="1" id="editValue" class="form-control" placeholder="Ex: 45.00">
          </div>
        </div>

        <div class="form-group">
          <label>Notes & Commentaires personnels</label>
          <textarea id="editNotes" class="form-control" rows="3" placeholder="Particularités, pions en métal spéciaux, historique d'achat..."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" id="cancelEditBtn">Annuler</button>
        <button class="btn btn-primary" id="saveEditBtn">Enregistrer les modifications</button>
      </div>
    </div>
  </div>

  <!-- MODAL: ADD CUSTOM EDITION -->
  <div class="modal-backdrop" id="addModalBackdrop">
    <div class="modal">
      <div class="modal-header">
        <h3>Ajouter une nouvelle édition</h3>
        <button class="close-btn" id="closeAddModal">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label>Nom de l'édition *</label>
          <input type="text" id="addName" class="form-control" placeholder="Ex: Monopoly Collector Nostalgia, Monopoly Bordeaux..." required>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Catégorie</label>
            <input type="text" id="addCategory" class="form-control" list="categoryOptions" placeholder="Sélectionner ou saisir...">
            <datalist id="categoryOptions"></datalist>
          </div>
          <div class="form-group">
            <label>Année de sortie</label>
            <input type="number" id="addYear" class="form-control" placeholder="Ex: 2022">
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Pays / Région</label>
            <input type="text" id="addCountry" class="form-control" placeholder="Ex: France, USA, Japon...">
          </div>
          <div class="form-group">
            <label>Éditeur</label>
            <input type="text" id="addPublisher" class="form-control" placeholder="Ex: Hasbro, Winning Moves...">
          </div>
        </div>

        <div class="form-group">
          <label>Photo de la boîte (URL ou Fichier local)</label>
          <div class="modal-image-preview-area">
            <div id="addModalImagePreview" class="preview-box-thumb"></div>
            <div class="image-inputs-col">
              <input type="text" id="addImageUrl" class="form-control" placeholder="Coller l'URL d'une photo...">
              <label class="btn btn-secondary" style="font-size: 0.8rem; padding: 6px 12px; cursor: pointer;">
                📸 Charger une photo locale
                <input type="file" id="addImageFileInput" accept="image/*" style="display: none;">
              </label>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label>Description & Pions inclus</label>
          <textarea id="addDescription" class="form-control" rows="2" placeholder="Détails du plateau, pions emblématiques..."></textarea>
        </div>

        <div class="form-group">
          <label>Statut initial</label>
          <select id="addStatus" class="form-control">
            <option value="owned">🟢 Déjà Possédé</option>
            <option value="wishlist">⭐ Recherché (Wishlist)</option>
            <option value="none">⚪ Non possédé (Dans le catalogue)</option>
          </select>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" id="cancelAddBtn">Annuler</button>
        <button class="btn btn-primary" id="confirmAddBtn">Créer l'édition</button>
      </div>
    </div>
  </div>

  <!-- LIGHTBOX MODAL: FULL SIZE BOX VIEWER -->
  <div class="modal-backdrop" id="lightboxModalBackdrop">
    <div class="modal lightbox-modal">
      <div class="modal-header">
        <h3 id="lightboxTitle">Jaquette Officielle</h3>
        <button class="close-btn" id="closeLightbox">&times;</button>
      </div>
      <div class="modal-body" style="align-items: center;">
        <div id="lightboxMediaContainer" style="width: 100%; min-height: 260px; display: flex; align-items: center; justify-content: center;"></div>
        <p id="lightboxDesc" style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.5; margin-top: 10px; text-align: left; width: 100%;"></p>
        <div id="lightboxMeta" style="display: flex; gap: 14px; justify-content: center; font-size: 0.85rem; font-weight: 600; margin-top: 6px; flex-wrap: wrap;"></div>
      </div>
      <div class="modal-footer" style="justify-content: center; gap: 12px;">
        <a id="lightboxGoogleBtn" class="btn btn-secondary" target="_blank" href="#">🔍 Comparer sur Google Images</a>
        <button class="btn btn-primary" id="lightboxEditBtn">✏️ Modifier la fiche ou la photo</button>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">Données enregistrées</div>

  <script>
    const SEED_DATA = __SEED_DATA__;
    const STORAGE_KEY = "monopoly_collection_db_v4";

    let database = [];
    let currentFilterStatus = "all";
    let currentFilterCategory = "all";
    let currentSearchTerm = "";
    let currentCountry = "all";
    let currentSort = "name-asc";
    let currentView = "card";
    let activeLightboxId = null;

    function handleImageError(img, id) {
      img.style.display = "none";
      const fallback = img.nextElementSibling;
      if (fallback) {
        fallback.style.display = "flex";
      }
    }

    function initDatabase() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try {
          const parsed = JSON.parse(saved);
          if (Array.isArray(parsed) && parsed.length > 0) {
            database = parsed;
          } else {
            loadFromSeed();
          }
        } catch(e) {
          loadFromSeed();
        }
      } else {
        loadFromSeed();
      }
    }

    function loadFromSeed() {
      database = SEED_DATA.map(function(item) {
        return Object.assign({}, item, {
          status: "none",
          condition: "",
          price: "",
          value: "",
          location: "",
          notes: ""
        });
      });
      saveDatabase();
    }

    function saveDatabase() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(database));
      renderStats();
      populateFilters();
    }

    function showToast(msg) {
      const toast = document.getElementById("toast");
      toast.textContent = msg;
      toast.classList.add("show");
      setTimeout(function() {
        toast.classList.remove("show");
      }, 2600);
    }

    function renderStats() {
      const total = database.length;
      const owned = database.filter(function(e) { return e.status === "owned"; }).length;
      const wishlist = database.filter(function(e) { return e.status === "wishlist"; }).length;
      const none = database.filter(function(e) { return e.status === "none" || !e.status; }).length;
      const withPhotos = database.filter(function(e) { return Boolean(e.image_url); }).length;

      let totalVal = 0;
      let totalSpent = 0;
      database.forEach(function(e) {
        if (e.status === "owned") {
          if (e.value) totalVal += parseFloat(e.value) || 0;
          if (e.price) totalSpent += parseFloat(e.price) || 0;
        }
      });

      const pct = total > 0 ? Math.round((owned / total) * 100) : 0;

      document.getElementById("statTotal").textContent = total;
      document.getElementById("statWithPhotos").textContent = withPhotos;
      document.getElementById("statOwned").textContent = owned;
      document.getElementById("statOwnedPct").textContent = "(" + pct + "%)";
      document.getElementById("statProgressBar").style.width = pct + "%";
      document.getElementById("statWishlist").textContent = wishlist;
      document.getElementById("statEstimatedValue").textContent = totalVal.toLocaleString('fr-FR', { minimumFractionDigits: 0, maximumFractionDigits: 2 }) + " €";
      document.getElementById("statSpentValue").textContent = totalSpent.toLocaleString('fr-FR', { minimumFractionDigits: 0, maximumFractionDigits: 2 }) + " €";

      document.getElementById("countAll").textContent = total;
      document.getElementById("countOwned").textContent = owned;
      document.getElementById("countWishlist").textContent = wishlist;
      document.getElementById("countNone").textContent = none;
    }

    function populateFilters() {
      const catMap = {};
      database.forEach(function(e) {
        if (e.category) catMap[e.category] = (catMap[e.category] || 0) + 1;
      });
      const categories = Object.keys(catMap).sort();

      const catContainer = document.getElementById("categoryPills");
      const currentActive = currentFilterCategory;

      catContainer.innerHTML = '<span class="pill ' + (currentActive === "all" ? "active" : "") + '" data-category="all">Toutes les catégories</span>';
      categories.forEach(function(cat) {
        const count = catMap[cat];
        const pill = document.createElement("span");
        pill.className = "pill " + (currentActive === cat ? "active" : "");
        pill.dataset.category = cat;
        pill.textContent = cat + " (" + count + ")";
        catContainer.appendChild(pill);
      });

      const datalist = document.getElementById("categoryOptions");
      datalist.innerHTML = "";
      categories.forEach(function(cat) {
        const opt = document.createElement("option");
        opt.value = cat;
        datalist.appendChild(opt);
      });

      const countrySet = {};
      database.forEach(function(e) {
        if (e.country) countrySet[e.country] = true;
      });
      const countries = Object.keys(countrySet).sort();

      const countrySelect = document.getElementById("countrySelect");
      const selectedVal = countrySelect.value;
      countrySelect.innerHTML = '<option value="all">Tous les Pays / Régions</option>';
      countries.forEach(function(c) {
        const opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        countrySelect.appendChild(opt);
      });
      if (countrySet[selectedVal]) {
        countrySelect.value = selectedVal;
      }
    }

    function getFilteredAndSortedEditions() {
      return database.filter(function(item) {
        if (currentFilterStatus === "owned" && item.status !== "owned") return false;
        if (currentFilterStatus === "wishlist" && item.status !== "wishlist") return false;
        if (currentFilterStatus === "none" && item.status !== "none" && item.status) return false;

        if (currentFilterCategory !== "all" && item.category !== currentFilterCategory) return false;
        if (currentCountry !== "all" && item.country !== currentCountry) return false;

        if (currentSearchTerm) {
          const term = currentSearchTerm.toLowerCase();
          const matchName = item.name && item.name.toLowerCase().includes(term);
          const matchDesc = item.description && item.description.toLowerCase().includes(term);
          const matchCat = item.category && item.category.toLowerCase().includes(term);
          const matchCountry = item.country && item.country.toLowerCase().includes(term);
          const matchPub = item.publisher && item.publisher.toLowerCase().includes(term);
          const matchNotes = item.notes && item.notes.toLowerCase().includes(term);
          const matchLoc = item.location && item.location.toLowerCase().includes(term);
          const matchYear = item.year && item.year.toString().includes(term);
          if (!matchName && !matchDesc && !matchCat && !matchCountry && !matchPub && !matchNotes && !matchLoc && !matchYear) {
            return false;
          }
        }
        return true;
      }).sort(function(a, b) {
        if (currentSort === "name-asc") return (a.name || "").localeCompare(b.name || "");
        if (currentSort === "name-desc") return (b.name || "").localeCompare(a.name || "");
        if (currentSort === "year-desc") return (b.year || 0) - (a.year || 0);
        if (currentSort === "year-asc") return (a.year || 0) - (b.year || 0);
        if (currentSort === "status") {
          const order = { owned: 1, wishlist: 2, none: 3 };
          return (order[a.status] || 3) - (order[b.status] || 3);
        }
        return 0;
      });
    }

    function renderList() {
      const filtered = getFilteredAndSortedEditions();
      const cardsContainer = document.getElementById("cardsContainer");
      const tableBody = document.getElementById("tableBody");
      const emptyState = document.getElementById("emptyState");

      if (filtered.length === 0) {
        emptyState.style.display = "block";
        cardsContainer.style.display = "none";
        document.getElementById("tableContainer").style.display = "none";
        return;
      }

      emptyState.style.display = "none";

      if (currentView === "card") {
        cardsContainer.style.display = "grid";
        document.getElementById("tableContainer").style.display = "none";
        renderCards(filtered, cardsContainer);
      } else {
        cardsContainer.style.display = "none";
        document.getElementById("tableContainer").style.display = "block";
        renderTable(filtered, tableBody);
      }
    }

    function renderCards(items, container) {
      container.innerHTML = "";
      items.forEach(function(item) {
        const card = document.createElement("div");
        card.className = "edition-card";

        const statusLabel = item.status === "owned" 
          ? "🟢 Possédé" 
          : item.status === "wishlist" 
          ? "⭐ Recherché" 
          : "⚪ Non possédé";

        const badgeClass = item.status === "owned" ? "owned" : item.status === "wishlist" ? "wishlist" : "none";

        const googleQuery = encodeURIComponent(item.name + " jeu boite");
        const googleUrl = "https://www.google.com/search?tbm=isch&q=" + googleQuery;

        // REAL BOX VISUAL RENDERING
        let coverHtml = "";
        if (item.image_url) {
          coverHtml = 
            '<img class="box-cover-image" src="' + item.image_url + '" alt="' + item.name + '" onerror="handleImageError(this, \'' + item.id + '\')">' +
            '<div class="missing-cover-box" style="display:none;">' +
              '<div class="missing-icon">📦</div>' +
              '<div class="missing-title">' + item.name + '</div>' +
              '<div class="missing-sub">Photo locale non trouvée</div>' +
            '</div>' +
            '<div class="verified-badge">📸 Photo Réelle</div>';
        } else {
          coverHtml = 
            '<div class="missing-cover-box">' +
              '<div class="missing-icon">📷</div>' +
              '<div class="missing-title">' + item.name + '</div>' +
              '<div class="missing-sub">Cliquer pour charger la photo de votre boîte</div>' +
            '</div>';
        }

        let userInfoHtml = "";
        if (item.status === "owned") {
          userInfoHtml = '<div class="card-user-info">';
          if (item.condition) userInfoHtml += '<div><strong>État:</strong> ' + item.condition + '</div>';
          if (item.location) userInfoHtml += '<div><strong>Emplacement:</strong> ' + item.location + '</div>';
          if (item.price || item.value) {
            userInfoHtml += '<div>' + (item.price ? 'Achat: ' + item.price + '€ ' : '') + (item.value ? '| Est.: ' + item.value + '€' : '') + '</div>';
          }
          if (item.notes) userInfoHtml += '<div><strong>Note:</strong> ' + item.notes + '</div>';
          userInfoHtml += '</div>';
        } else if (item.status === "wishlist" && (item.notes || item.value)) {
          userInfoHtml = '<div class="card-user-info">';
          if (item.value) userInfoHtml += '<div>Budget max: ' + item.value + '€</div>';
          if (item.notes) userInfoHtml += '<div>' + item.notes + '</div>';
          userInfoHtml += '</div>';
        }

        card.innerHTML = 
          '<div class="box-cover-wrapper" data-lightbox-id="' + item.id + '" title="Cliquer pour inspecter la jaquette en grand format">' +
            '<div class="status-ribbon ' + badgeClass + '">' + statusLabel + '</div>' +
            coverHtml +
          '</div>' +
          '<div class="card-body">' +
            '<div class="card-top">' +
              '<span class="card-category">' + (item.category || 'Général') + '</span>' +
              '<span class="card-year">' + (item.year || 'N/C') + '</span>' +
            '</div>' +
            '<h3 class="card-title">' + item.name + '</h3>' +
            '<p class="card-desc">' + (item.description || 'Édition officielle Monopoly.') + '</p>' +
            '<div class="card-meta">' +
              '<span class="meta-item">📍 ' + (item.country || 'International') + '</span>' +
              '<span class="meta-item">🏢 ' + (item.publisher || 'Hasbro') + '</span>' +
            '</div>' +
            userInfoHtml +
            '<div class="card-actions">' +
              '<span class="status-badge ' + badgeClass + '" data-id="' + item.id + '" title="Cliquer pour changer le statut">' + statusLabel + '</span>' +
              '<div style="display:flex; gap:6px;">' +
                '<a class="btn-google" href="' + googleUrl + '" target="_blank" title="Rechercher des photos sur Google Images">🔍 Google</a>' +
                '<button class="btn btn-secondary edit-btn" data-id="' + item.id + '" style="padding: 5px 10px; font-size: 0.8rem;">✏️ Modifier</button>' +
              '</div>' +
            '</div>' +
          '</div>';
        
        container.appendChild(card);
      });
    }

    function renderTable(items, tbody) {
      tbody.innerHTML = "";
      items.forEach(function(item) {
        const tr = document.createElement("tr");
        const statusLabel = item.status === "owned" 
          ? "🟢 Possédé" 
          : item.status === "wishlist" 
          ? "⭐ Recherché" 
          : "⚪ Non possédé";
        const badgeClass = item.status === "owned" ? "owned" : item.status === "wishlist" ? "wishlist" : "none";

        let thumbHtml = "";
        if (item.image_url) {
          thumbHtml = '<img class="table-thumb" src="' + item.image_url + '" alt="Boîte" data-lightbox-id="' + item.id + '" onerror="this.src=\'data:image/svg+xml;utf8,<svg xmlns=\\\'http://www.w3.org/2000/svg\\\' width=\\\'50\\\' height=\\\'35\\\'><rect width=\\\'50\\\' height=\\\'35\\\' fill=\\\'%23334155\\\'/><text x=\\\'25\\\' y=\\\'22\\\' fill=\\\'white\\\' font-size=\\\'10\\\' text-anchor=\\\'middle\\\'>📦</text></svg>\';">';
        } else {
          thumbHtml = '<div class="table-thumb" data-lightbox-id="' + item.id + '" style="display: flex; align-items: center; justify-content: center; font-size: 11px; color: #94a3b8;">📷</div>';
        }

        tr.innerHTML = 
          '<td>' + thumbHtml + '</td>' +
          '<td><span class="status-badge ' + badgeClass + '" data-id="' + item.id + '">' + statusLabel + '</span></td>' +
          '<td><strong>' + item.name + '</strong></td>' +
          '<td><span class="card-category">' + (item.category || '-') + '</span></td>' +
          '<td>' + (item.year || '-') + '</td>' +
          '<td>' + (item.country || '-') + '</td>' +
          '<td>' + (item.condition || '-') + '</td>' +
          '<td>' + (item.price ? item.price + ' €' : '-') + '</td>' +
          '<td>' + (item.value ? item.value + ' €' : '-') + '</td>' +
          '<td>' +
            '<button class="btn btn-secondary edit-btn" data-id="' + item.id + '" style="padding: 4px 10px; font-size: 0.8rem;">✏️ Éditer</button>' +
          '</td>';
        tbody.appendChild(tr);
      });
    }

    function cycleStatus(id) {
      const item = database.find(function(e) { return e.id === id; });
      if (!item) return;
      if (item.status === "none" || !item.status) {
        item.status = "owned";
      } else if (item.status === "owned") {
        item.status = "wishlist";
      } else {
        item.status = "none";
      }
      saveDatabase();
      renderList();
      showToast('Statut mis à jour : "' + item.name + '" -> ' + (item.status === "owned" ? "Possédé" : item.status === "wishlist" ? "Recherché" : "Non possédé"));
    }

    // LIGHTBOX FULL VIEWER
    function openLightbox(id) {
      const item = database.find(function(e) { return e.id === id; });
      if (!item) return;
      activeLightboxId = id;

      document.getElementById("lightboxTitle").textContent = item.name;
      document.getElementById("lightboxDesc").textContent = item.description || "Édition officielle Monopoly.";
      document.getElementById("lightboxMeta").innerHTML = 
        '<span>Année : ' + (item.year || 'N/C') + '</span> &bull; ' +
        '<span>Catégorie : ' + (item.category || 'Général') + '</span> &bull; ' +
        '<span>Éditeur : ' + (item.publisher || 'Hasbro') + '</span>';

      const googleQuery = encodeURIComponent(item.name + " jeu boite");
      document.getElementById("lightboxGoogleBtn").href = "https://www.google.com/search?tbm=isch&q=" + googleQuery;

      const mediaContainer = document.getElementById("lightboxMediaContainer");
      if (item.image_url) {
        mediaContainer.innerHTML = '<img class="lightbox-img" src="' + item.image_url + '" alt="' + item.name + '">';
      } else {
        mediaContainer.innerHTML = 
          '<div style="width: 100%; max-width: 440px; height: 260px; border-radius: 12px; background: #090d16; display: flex; flex-direction: column; align-items: center; justify-content: center; border: 1px dashed var(--border-color); gap: 10px;">' +
            '<span style="font-size: 3rem;">📷</span>' +
            '<span style="font-weight: 700; color: var(--text-main); font-size: 1.1rem;">Aucune photo enregistrée</span>' +
            '<span style="font-size: 0.85rem; color: var(--text-muted); max-width: 80%;">Utilisez le bouton ci-dessous pour charger la photo de votre boîte ou la chercher sur Google Images.</span>' +
          '</div>';
      }

      document.getElementById("lightboxModalBackdrop").classList.add("open");
    }

    // EDIT MODAL
    function openEditModal(id) {
      const item = database.find(function(e) { return e.id === id; });
      if (!item) return;

      document.getElementById("editItemId").value = id;
      document.getElementById("editModalTitle").textContent = item.name;
      document.getElementById("editStatus").value = item.status || "none";
      document.getElementById("editCondition").value = item.condition || "";
      document.getElementById("editLocation").value = item.location || "";
      document.getElementById("editPrice").value = item.price || "";
      document.getElementById("editValue").value = item.value || "";
      document.getElementById("editNotes").value = item.notes || "";
      document.getElementById("editImageUrl").value = item.image_url || "";

      const googleQuery = encodeURIComponent(item.name + " jeu boite");
      document.getElementById("modalGoogleSearchBtn").href = "https://www.google.com/search?tbm=isch&q=" + googleQuery;

      updateEditPreview(item);

      document.getElementById("editModalBackdrop").classList.add("open");
    }

    function updateEditPreview(item) {
      const preview = document.getElementById("modalImagePreviewContainer");
      const url = document.getElementById("editImageUrl").value.trim();
      if (url) {
        preview.innerHTML = '<img src="' + url + '" style="width:100%; height:100%; object-fit:contain; border-radius:4px;">';
      } else {
        preview.innerHTML = '<span style="font-size:1.8rem; opacity:0.6;">📷</span>';
      }
    }

    function saveEditModal() {
      const id = document.getElementById("editItemId").value;
      const item = database.find(function(e) { return e.id === id; });
      if (!item) return;

      item.status = document.getElementById("editStatus").value;
      item.condition = document.getElementById("editCondition").value;
      item.location = document.getElementById("editLocation").value.trim();
      item.price = document.getElementById("editPrice").value;
      item.value = document.getElementById("editValue").value;
      item.notes = document.getElementById("editNotes").value.trim();
      item.image_url = document.getElementById("editImageUrl").value.trim();

      document.getElementById("editModalBackdrop").classList.remove("open");
      saveDatabase();
      renderList();
      showToast("Fiche et photo enregistrées avec succès !");
    }

    // ADD CUSTOM EDITION MODAL
    function openAddModal() {
      document.getElementById("addName").value = "";
      document.getElementById("addCategory").value = "";
      document.getElementById("addYear").value = new Date().getFullYear();
      document.getElementById("addCountry").value = "";
      document.getElementById("addPublisher").value = "Hasbro";
      document.getElementById("addImageUrl").value = "";
      document.getElementById("addDescription").value = "";
      document.getElementById("addStatus").value = "owned";
      document.getElementById("addModalImagePreview").innerHTML = '<span style="font-size:1.8rem; opacity:0.6;">📷</span>';
      document.getElementById("addModalBackdrop").classList.add("open");
    }

    function saveCustomEdition() {
      const name = document.getElementById("addName").value.trim();
      if (!name) {
        alert("Veuillez saisir le nom de l'édition.");
        return;
      }

      const newId = "custom-" + Date.now();
      const newEdition = {
        id: newId,
        name: name,
        category: document.getElementById("addCategory").value.trim() || "Personnalisée",
        year: parseInt(document.getElementById("addYear").value, 10) || new Date().getFullYear(),
        country: document.getElementById("addCountry").value.trim() || "France",
        publisher: document.getElementById("addPublisher").value.trim() || "Hasbro",
        description: document.getElementById("addDescription").value.trim() || "Édition ajoutée par le collectionneur.",
        image_url: document.getElementById("addImageUrl").value.trim() || "",
        status: document.getElementById("addStatus").value,
        condition: "",
        price: "",
        value: "",
        location: "",
        notes: ""
      };

      database.unshift(newEdition);
      document.getElementById("addModalBackdrop").classList.remove("open");
      saveDatabase();
      renderList();
      showToast('Édition "' + name + '" créée avec succès !');
    }

    // EXPORT & BACKUP
    function exportToCsv() {
      const headers = ["ID", "Statut", "Nom", "Categorie", "Annee", "Pays", "Editeur", "Image_URL", "Etat", "Prix_Achat_EUR", "Valeur_Estimee_EUR", "Emplacement", "Notes", "Description"];
      const rows = database.map(function(e) {
        return [
          '"' + (e.id || '').replace(/"/g, '""') + '"',
          '"' + (e.status === 'owned' ? 'Possédé' : e.status === 'wishlist' ? 'Recherché' : 'Non possédé').replace(/"/g, '""') + '"',
          '"' + (e.name || '').replace(/"/g, '""') + '"',
          '"' + (e.category || '').replace(/"/g, '""') + '"',
          '"' + (e.year || '') + '"',
          '"' + (e.country || '').replace(/"/g, '""') + '"',
          '"' + (e.publisher || '').replace(/"/g, '""') + '"',
          '"' + (e.image_url || '').replace(/"/g, '""') + '"',
          '"' + (e.condition || '').replace(/"/g, '""') + '"',
          '"' + (e.price || '') + '"',
          '"' + (e.value || '') + '"',
          '"' + (e.location || '').replace(/"/g, '""') + '"',
          '"' + (e.notes || '').replace(/"/g, '""') + '"',
          '"' + (e.description || '').replace(/"/g, '""') + '"'
        ];
      });

      const csvContent = "\uFEFF" + headers.join(";") + "\n" + rows.map(function(r) { return r.join(";"); }).join("\n");
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "monopoly_collection_" + new Date().toISOString().slice(0,10) + ".csv";
      a.click();
      URL.revokeObjectURL(url);
      showToast("Fichier CSV exporté pour Excel !");
    }

    function backupToJson() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(database, null, 2));
      const a = document.createElement("a");
      a.href = dataStr;
      a.download = "monopoly_collection_backup_" + new Date().toISOString().slice(0,10) + ".json";
      a.click();
      showToast("Sauvegarde JSON téléchargée !");
    }

    function importFromJson(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(event) {
        try {
          const imported = JSON.parse(event.target.result);
          if (Array.isArray(imported)) {
            database = imported;
            saveDatabase();
            renderList();
            showToast("Collection restaurée avec succès !");
          } else {
            alert("Format JSON non valide.");
          }
        } catch(err) {
          alert("Erreur lors de la lecture du fichier : " + err.message);
        }
      };
      reader.readAsText(file);
      e.target.value = "";
    }

    function handleImageUpload(file, inputTargetId, previewContainerId) {
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        const dataUrl = e.target.result;
        document.getElementById(inputTargetId).value = dataUrl;
        document.getElementById(previewContainerId).innerHTML = '<img src="' + dataUrl + '" style="width:100%; height:100%; object-fit:contain; border-radius:4px;">';
      };
      reader.readAsDataURL(file);
    }

    // INITIALIZATION & LISTENERS
    document.addEventListener("DOMContentLoaded", function() {
      initDatabase();
      renderStats();
      populateFilters();
      renderList();

      document.getElementById("themeBtn").addEventListener("click", function() {
        const body = document.body;
        const newTheme = body.getAttribute("data-theme") === "light" ? "dark" : "light";
        body.setAttribute("data-theme", newTheme);
      });

      document.getElementById("searchInput").addEventListener("input", function(e) {
        currentSearchTerm = e.target.value.trim();
        renderList();
      });

      document.getElementById("countrySelect").addEventListener("change", function(e) {
        currentCountry = e.target.value;
        renderList();
      });

      document.getElementById("sortSelect").addEventListener("change", function(e) {
        currentSort = e.target.value;
        renderList();
      });

      document.getElementById("cardViewBtn").addEventListener("click", function() {
        currentView = "card";
        document.getElementById("cardViewBtn").classList.add("active");
        document.getElementById("tableViewBtn").classList.remove("active");
        renderList();
      });

      document.getElementById("tableViewBtn").addEventListener("click", function() {
        currentView = "table";
        document.getElementById("tableViewBtn").classList.add("active");
        document.getElementById("cardViewBtn").classList.remove("active");
        renderList();
      });

      document.getElementById("statusPills").addEventListener("click", function(e) {
        const pill = e.target.closest(".pill");
        if (!pill) return;
        document.querySelectorAll("#statusPills .pill").forEach(function(p) { p.classList.remove("active"); });
        pill.classList.add("active");
        currentFilterStatus = pill.dataset.status;
        renderList();
      });

      document.getElementById("categoryPills").addEventListener("click", function(e) {
        const pill = e.target.closest(".pill");
        if (!pill) return;
        document.querySelectorAll("#categoryPills .pill").forEach(function(p) { p.classList.remove("active"); });
        pill.classList.add("active");
        currentFilterCategory = pill.dataset.category;
        renderList();
      });

      // Global delegation
      document.addEventListener("click", function(e) {
        const badge = e.target.closest(".status-badge");
        if (badge && badge.dataset.id) {
          cycleStatus(badge.dataset.id);
          return;
        }

        const editBtn = e.target.closest(".edit-btn");
        if (editBtn && editBtn.dataset.id) {
          openEditModal(editBtn.dataset.id);
          return;
        }

        const boxWrapper = e.target.closest(".box-cover-wrapper, [data-lightbox-id]");
        if (boxWrapper && boxWrapper.dataset.lightboxId && !e.target.closest(".status-ribbon")) {
          openLightbox(boxWrapper.dataset.lightboxId);
          return;
        }
      });

      // Edit Modal Actions
      document.getElementById("closeEditModal").addEventListener("click", function() {
        document.getElementById("editModalBackdrop").classList.remove("open");
      });
      document.getElementById("cancelEditBtn").addEventListener("click", function() {
        document.getElementById("editModalBackdrop").classList.remove("open");
      });
      document.getElementById("saveEditBtn").addEventListener("click", saveEditModal);

      document.getElementById("editImageUrl").addEventListener("input", function() {
        const id = document.getElementById("editItemId").value;
        const item = database.find(function(e) { return e.id === id; });
        updateEditPreview(item);
      });

      document.getElementById("editImageFileInput").addEventListener("change", function(e) {
        handleImageUpload(e.target.files[0], "editImageUrl", "modalImagePreviewContainer");
      });

      document.getElementById("clearImageBtn").addEventListener("click", function() {
        document.getElementById("editImageUrl").value = "";
        const id = document.getElementById("editItemId").value;
        const item = database.find(function(e) { return e.id === id; });
        updateEditPreview(item);
      });

      // Lightbox Actions
      document.getElementById("closeLightbox").addEventListener("click", function() {
        document.getElementById("lightboxModalBackdrop").classList.remove("open");
      });
      document.getElementById("lightboxEditBtn").addEventListener("click", function() {
        document.getElementById("lightboxModalBackdrop").classList.remove("open");
        if (activeLightboxId) openEditModal(activeLightboxId);
      });

      // Add Modal Actions
      document.getElementById("addCustomBtn").addEventListener("click", openAddModal);
      document.getElementById("closeAddModal").addEventListener("click", function() {
        document.getElementById("addModalBackdrop").classList.remove("open");
      });
      document.getElementById("cancelAddBtn").addEventListener("click", function() {
        document.getElementById("addModalBackdrop").classList.remove("open");
      });
      document.getElementById("confirmAddBtn").addEventListener("click", saveCustomEdition);

      document.getElementById("addImageUrl").addEventListener("input", function(e) {
        const url = e.target.value.trim();
        const preview = document.getElementById("addModalImagePreview");
        if (url) {
          preview.innerHTML = '<img src="' + url + '" style="width:100%; height:100%; object-fit:contain; border-radius:4px;">';
        } else {
          preview.innerHTML = '<span style="font-size:1.8rem; opacity:0.6;">📷</span>';
        }
      });

      document.getElementById("addImageFileInput").addEventListener("change", function(e) {
        handleImageUpload(e.target.files[0], "addImageUrl", "addModalImagePreview");
      });

      // Export / Import
      document.getElementById("exportCsvBtn").addEventListener("click", exportToCsv);
      document.getElementById("backupJsonBtn").addEventListener("click", backupToJson);
      document.getElementById("importJsonInput").addEventListener("change", importFromJson);
    });
  </script>
</body>
</html>
"""

final_html = html_template.replace("__SEED_DATA__", json_str)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated index.html with real box images!")
