# -*- coding: utf-8 -*-
import json

with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/editions_seed.json", "r", encoding="utf-8") as f:
    seed_data = json.load(f)

json_str = json.dumps(seed_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Monopoly Collector Hub - Suivi de Collection</title>
  <style>
    :root {
      --bg-main: #0f172a;
      --bg-card: #1e293b;
      --bg-card-hover: #26354a;
      --bg-surface: #1e293b;
      --border-color: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #e11d48;
      --primary-hover: #be123c;
      --accent: #38bdf8;
      --success: #10b981;
      --warning: #f59e0b;
      --tag-bg: rgba(56, 189, 248, 0.12);
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -2px rgba(0, 0, 0, 0.2);
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
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
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
      background: linear-gradient(135deg, #be123c 0%, #1e293b 100%);
      padding: 24px 20px 20px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.25);
      border-bottom: 2px solid #e11d48;
    }

    .header-content {
      max-width: 1400px;
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
      font-size: 28px;
      color: white;
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.4);
      border: 2px solid #fff;
    }

    .header-title h1 {
      font-size: 1.7rem;
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
      padding: 9px 16px;
      border-radius: 8px;
      font-size: 0.88rem;
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

    .btn-success {
      background-color: var(--success);
      color: white;
    }
    .btn-success:hover {
      opacity: 0.9;
    }

    .container {
      max-width: 1400px;
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
      font-size: 1.8rem;
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

    .filter-select:focus {
      border-color: var(--accent);
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
      gap: 20px;
    }

    .edition-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .edition-card:hover {
      transform: translateY(-3px);
      border-color: rgba(56, 189, 248, 0.4);
    }

    .edition-card.status-owned {
      border-left: 5px solid var(--success);
    }
    .edition-card.status-wishlist {
      border-left: 5px solid var(--warning);
    }
    .edition-card.status-none {
      border-left: 5px solid transparent;
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
    }

    .card-category {
      font-size: 0.75rem;
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
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .card-title {
      font-size: 1.12rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
    }

    .card-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
      flex-grow: 1;
    }

    .card-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.8rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border-color);
      padding-top: 12px;
    }

    .meta-item {
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 10px;
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

    .card-user-info {
      background: rgba(0,0,0,0.15);
      border-radius: 6px;
      padding: 8px 10px;
      font-size: 0.8rem;
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
      padding-top: 8px;
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
      font-size: 0.9rem;
    }

    th {
      background: rgba(0,0,0,0.2);
      padding: 14px 16px;
      font-weight: 700;
      color: var(--text-muted);
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }

    td {
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
    }

    tr:hover td {
      background: rgba(255,255,255,0.02);
    }

    /* MODAL */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(4px);
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
      max-width: 600px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5);
      transform: translateY(20px);
      transition: transform 0.2s ease;
    }

    .modal-backdrop.open .modal {
      transform: translateY(0);
    }

    .modal-header {
      padding: 20px 24px;
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
      padding: 24px;
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

    .empty-state {
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
    }

    .empty-state svg {
      width: 64px;
      height: 64px;
      margin-bottom: 16px;
      opacity: 0.4;
    }

    /* Toast Notification */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: white;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      z-index: 1000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s ease;
    }

    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    @media print {
      header, .controls-panel, .header-actions, .card-actions, .modal-backdrop {
        display: none !important;
      }
      body {
        background: white !important;
        color: black !important;
      }
      .stat-card, .edition-card, .table-container {
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        background: white !important;
        color: black !important;
      }
    }

    @media (max-width: 768px) {
      .form-row {
        grid-template-columns: 1fr;
      }
      .search-box {
        min-width: 100%;
      }
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
          <p>Gestionnaire & inventaire de collection Monopoly mondial</p>
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
        <div class="stat-sub">Base de données mondiale</div>
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
          <button class="view-btn active" id="cardViewBtn" title="Vue Cartes">🗂️ Cartes</button>
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
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="8" y1="12" x2="16" y2="12"></line>
      </svg>
      <h3>Aucune édition ne correspond à vos filtres</h3>
      <p style="margin-top: 6px;">Essayez d'ajuster votre recherche ou réinitialisez les filtres.</p>
    </div>

  </div>

  <!-- MODAL: EDIT USER DETAILS -->
  <div class="modal-backdrop" id="editModalBackdrop">
    <div class="modal">
      <div class="modal-header">
        <h3 id="editModalTitle">Détails de l'édition</h3>
        <button class="close-btn" id="closeEditModal">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="editItemIndex">

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
            <label>État du jeu</label>
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
            <input type="text" id="editLocation" class="form-control" placeholder="Ex: Étagère A, Salon, Carton 2...">
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
          <textarea id="editNotes" class="form-control" rows="3" placeholder="Particularités, pièces spécifiques, historique d'achat..."></textarea>
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
          <input type="text" id="addName" class="form-control" placeholder="Ex: Monopoly Vintage 1960, Monopoly Bretagne..." required>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Catégorie</label>
            <input type="text" id="addCategory" class="form-control" list="categoryOptions" placeholder="Sélectionner ou saisir...">
            <datalist id="categoryOptions"></datalist>
          </div>
          <div class="form-group">
            <label>Année de sortie</label>
            <input type="number" id="addYear" class="form-control" placeholder="Ex: 2015">
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Pays / Région</label>
            <input type="text" id="addCountry" class="form-control" placeholder="Ex: France, USA, Japon...">
          </div>
          <div class="form-group">
            <label>Éditeur / Fabricant</label>
            <input type="text" id="addPublisher" class="form-control" placeholder="Ex: Hasbro, Winning Moves, USAopoly...">
          </div>
        </div>

        <div class="form-group">
          <label>Description & Pions inclus</label>
          <textarea id="addDescription" class="form-control" rows="2" placeholder="Détails du plateau, pions emblématiques, spécificités..."></textarea>
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

  <div class="toast" id="toast">Données enregistrées avec succès</div>

  <script>
    // BASE DATABASE (Seed)
    const SEED_DATA = __SEED_DATA__;

    const STORAGE_KEY = "monopoly_collection_db_v1";

    let database = [];
    let currentFilterStatus = "all";
    let currentFilterCategory = "all";
    let currentSearchTerm = "";
    let currentCountry = "all";
    let currentSort = "name-asc";
    let currentView = "card";

    function initDatabase() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try {
          database = JSON.parse(saved);
        } catch(e) {
          console.error("Error loading localStorage, using seed", e);
          database = SEED_DATA.map(item => ({ ...item, status: "none", condition: "", price: "", value: "", location: "", notes: "" }));
        }
      } else {
        database = SEED_DATA.map(item => ({
          ...item,
          status: "none",
          condition: "",
          price: "",
          value: "",
          location: "",
          notes: ""
        }));
        saveDatabase();
      }
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
      setTimeout(() => toast.classList.remove("show"), 2800);
    }

    function renderStats() {
      const total = database.length;
      const owned = database.filter(e => e.status === "owned").length;
      const wishlist = database.filter(e => e.status === "wishlist").length;
      const none = database.filter(e => e.status === "none" || !e.status).length;

      let totalVal = 0;
      let totalSpent = 0;
      database.forEach(e => {
        if (e.status === "owned") {
          if (e.value) totalVal += parseFloat(e.value) || 0;
          if (e.price) totalSpent += parseFloat(e.price) || 0;
        }
      });

      const pct = total > 0 ? Math.round((owned / total) * 100) : 0;

      document.getElementById("statTotal").textContent = total;
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
      // Categories
      const categories = Array.from(new Set(database.map(e => e.category).filter(Boolean))).sort();
      const catContainer = document.getElementById("categoryPills");
      const currentActive = currentFilterCategory;

      catContainer.innerHTML = '<span class="pill ' + (currentActive === "all" ? "active" : "") + '" data-category="all">Toutes les catégories</span>';
      categories.forEach(cat => {
        const count = database.filter(e => e.category === cat).length;
        const pill = document.createElement("span");
        pill.className = "pill " + (currentActive === cat ? "active" : "");
        pill.dataset.category = cat;
        pill.textContent = cat + " (" + count + ")";
        catContainer.appendChild(pill);
      });

      // Datalist for custom edition
      const datalist = document.getElementById("categoryOptions");
      datalist.innerHTML = "";
      categories.forEach(cat => {
        const opt = document.createElement("option");
        opt.value = cat;
        datalist.appendChild(opt);
      });

      // Countries
      const countries = Array.from(new Set(database.map(e => e.country).filter(Boolean))).sort();
      const countrySelect = document.getElementById("countrySelect");
      const selectedVal = countrySelect.value;
      countrySelect.innerHTML = '<option value="all">Tous les Pays / Régions</option>';
      countries.forEach(c => {
        const opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        countrySelect.appendChild(opt);
      });
      if (countries.includes(selectedVal)) {
        countrySelect.value = selectedVal;
      }
    }

    function getFilteredAndSortedEditions() {
      return database.filter(item => {
        // Status filter
        if (currentFilterStatus === "owned" && item.status !== "owned") return false;
        if (currentFilterStatus === "wishlist" && item.status !== "wishlist") return false;
        if (currentFilterStatus === "none" && item.status !== "none" && item.status) return false;

        // Category filter
        if (currentFilterCategory !== "all" && item.category !== currentFilterCategory) return false;

        // Country filter
        if (currentCountry !== "all" && item.country !== currentCountry) return false;

        // Search term
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
      }).sort((a, b) => {
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
      items.forEach(item => {
        const card = document.createElement("div");
        card.className = "edition-card status-" + (item.status || "none");

        const statusLabel = item.status === "owned" 
          ? "🟢 Possédé" 
          : item.status === "wishlist" 
          ? "⭐ Recherché" 
          : "⚪ Non possédé";

        const badgeClass = item.status === "owned" ? "owned" : item.status === "wishlist" ? "wishlist" : "none";

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
            '<span class="status-badge ' + badgeClass + '" data-id="' + item.id + '" title="Cliquez pour basculer le statut">' + statusLabel + '</span>' +
            '<button class="btn btn-secondary edit-btn" data-id="' + item.id + '" style="padding: 5px 12px; font-size: 0.8rem;">✏️ Détails</button>' +
          '</div>';
        
        container.appendChild(card);
      });
    }

    function renderTable(items, tbody) {
      tbody.innerHTML = "";
      items.forEach(item => {
        const tr = document.createElement("tr");
        const statusLabel = item.status === "owned" 
          ? "🟢 Possédé" 
          : item.status === "wishlist" 
          ? "⭐ Recherché" 
          : "⚪ Non possédé";
        const badgeClass = item.status === "owned" ? "owned" : item.status === "wishlist" ? "wishlist" : "none";

        tr.innerHTML = 
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

    // TOGGLE STATUS DIRECTLY
    function cycleStatus(id) {
      const item = database.find(e => e.id === id);
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

    // EDIT MODAL
    function openEditModal(id) {
      const item = database.find(e => e.id === id);
      if (!item) return;

      document.getElementById("editItemIndex").value = id;
      document.getElementById("editModalTitle").textContent = item.name;
      document.getElementById("editStatus").value = item.status || "none";
      document.getElementById("editCondition").value = item.condition || "";
      document.getElementById("editLocation").value = item.location || "";
      document.getElementById("editPrice").value = item.price || "";
      document.getElementById("editValue").value = item.value || "";
      document.getElementById("editNotes").value = item.notes || "";

      document.getElementById("editModalBackdrop").classList.add("open");
    }

    function saveEditModal() {
      const id = document.getElementById("editItemIndex").value;
      const item = database.find(e => e.id === id);
      if (!item) return;

      item.status = document.getElementById("editStatus").value;
      item.condition = document.getElementById("editCondition").value;
      item.location = document.getElementById("editLocation").value.trim();
      item.price = document.getElementById("editPrice").value;
      item.value = document.getElementById("editValue").value;
      item.notes = document.getElementById("editNotes").value.trim();

      document.getElementById("editModalBackdrop").classList.remove("open");
      saveDatabase();
      renderList();
      showToast("Fiche édition enregistrée !");
    }

    // ADD CUSTOM EDITION MODAL
    function openAddModal() {
      document.getElementById("addName").value = "";
      document.getElementById("addCategory").value = "";
      document.getElementById("addYear").value = new Date().getFullYear();
      document.getElementById("addCountry").value = "";
      document.getElementById("addPublisher").value = "Hasbro";
      document.getElementById("addDescription").value = "";
      document.getElementById("addStatus").value = "owned";
      document.getElementById("addModalBackdrop").classList.add("open");
    }

    function saveCustomEdition() {
      const name = document.getElementById("addName").value.trim();
      if (!name) {
        alert("Veuillez entrer le nom de l'édition.");
        return;
      }

      const newId = "custom-" + Date.now();
      const newEdition = {
        id: newId,
        name: name,
        category: document.getElementById("addCategory").value.trim() || "Personnalisée",
        year: parseInt(document.getElementById("addYear").value) || new Date().getFullYear(),
        country: document.getElementById("addCountry").value.trim() || "France",
        publisher: document.getElementById("addPublisher").value.trim() || "Hasbro",
        description: document.getElementById("addDescription").value.trim() || "Édition ajoutée par le collectionneur.",
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
      showToast('Édition "' + name + '" ajoutée avec succès !');
    }

    // EXPORT & BACKUP
    function exportToCsv() {
      const headers = ["ID", "Statut", "Nom", "Categorie", "Annee", "Pays", "Editeur", "Etat", "Prix_Achat_EUR", "Valeur_Estimee_EUR", "Emplacement", "Notes", "Description"];
      const rows = database.map(e => [
        '"' + (e.id || '').replace(/"/g, '""') + '"',
        '"' + (e.status === 'owned' ? 'Possédé' : e.status === 'wishlist' ? 'Recherché' : 'Non possédé').replace(/"/g, '""') + '"',
        '"' + (e.name || '').replace(/"/g, '""') + '"',
        '"' + (e.category || '').replace(/"/g, '""') + '"',
        '"' + (e.year || '') + '"',
        '"' + (e.country || '').replace(/"/g, '""') + '"',
        '"' + (e.publisher || '').replace(/"/g, '""') + '"',
        '"' + (e.condition || '').replace(/"/g, '""') + '"',
        '"' + (e.price || '') + '"',
        '"' + (e.value || '') + '"',
        '"' + (e.location || '').replace(/"/g, '""') + '"',
        '"' + (e.notes || '').replace(/"/g, '""') + '"',
        '"' + (e.description || '').replace(/"/g, '""') + '"'
      ]);

      const csvContent = "\\uFEFF" + headers.join(";") + "\\n" + rows.map(r => r.join(";")).join("\\n");
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
            alert("Format JSON invalide.");
          }
        } catch(err) {
          alert("Erreur lors de la lecture du fichier JSON : " + err.message);
        }
      };
      reader.readAsText(file);
      e.target.value = "";
    }

    // EVENT LISTENERS
    document.addEventListener("DOMContentLoaded", () => {
      initDatabase();
      renderStats();
      populateFilters();
      renderList();

      // Theme toggle
      document.getElementById("themeBtn").addEventListener("click", () => {
        const body = document.body;
        const newTheme = body.getAttribute("data-theme") === "light" ? "dark" : "light";
        body.setAttribute("data-theme", newTheme);
      });

      // Search input
      document.getElementById("searchInput").addEventListener("input", (e) => {
        currentSearchTerm = e.target.value.trim();
        renderList();
      });

      // Country select
      document.getElementById("countrySelect").addEventListener("change", (e) => {
        currentCountry = e.target.value;
        renderList();
      });

      // Sort select
      document.getElementById("sortSelect").addEventListener("change", (e) => {
        currentSort = e.target.value;
        renderList();
      });

      // View toggle
      document.getElementById("cardViewBtn").addEventListener("click", () => {
        currentView = "card";
        document.getElementById("cardViewBtn").classList.add("active");
        document.getElementById("tableViewBtn").classList.remove("active");
        renderList();
      });

      document.getElementById("tableViewBtn").addEventListener("click", () => {
        currentView = "table";
        document.getElementById("tableViewBtn").classList.add("active");
        document.getElementById("cardViewBtn").classList.remove("active");
        renderList();
      });

      // Status pills
      document.getElementById("statusPills").addEventListener("click", (e) => {
        const pill = e.target.closest(".pill");
        if (!pill) return;
        document.querySelectorAll("#statusPills .pill").forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        currentFilterStatus = pill.dataset.status;
        renderList();
      });

      // Category pills
      document.getElementById("categoryPills").addEventListener("click", (e) => {
        const pill = e.target.closest(".pill");
        if (!pill) return;
        document.querySelectorAll("#categoryPills .pill").forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        currentFilterCategory = pill.dataset.category;
        renderList();
      });

      // Global click delegator for Status Toggle and Edit Button
      document.addEventListener("click", (e) => {
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
      });

      // Edit modal actions
      document.getElementById("closeEditModal").addEventListener("click", () => {
        document.getElementById("editModalBackdrop").classList.remove("open");
      });
      document.getElementById("cancelEditBtn").addEventListener("click", () => {
        document.getElementById("editModalBackdrop").classList.remove("open");
      });
      document.getElementById("saveEditBtn").addEventListener("click", saveEditModal);

      // Add modal actions
      document.getElementById("addCustomBtn").addEventListener("click", openAddModal);
      document.getElementById("closeAddModal").addEventListener("click", () => {
        document.getElementById("addModalBackdrop").classList.remove("open");
      });
      document.getElementById("cancelAddBtn").addEventListener("click", () => {
        document.getElementById("addModalBackdrop").classList.remove("open");
      });
      document.getElementById("confirmAddBtn").addEventListener("click", saveCustomEdition);

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

with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("index.html created successfully!")
