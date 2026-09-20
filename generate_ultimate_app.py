# -*- coding: utf-8 -*-
"""
Ultimate Monopoly Tracker Web Application Generator.
Loads 1,189+ editions and builds an ultra-performant, responsive offline app.
"""
import json
import re

with open("editions_seed.json", "r", encoding="utf-8") as f:
    seed_data = json.load(f)

print(f"Loaded {len(seed_data)} editions from seed.")

seed_json_str = json.dumps(seed_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Monopoly Collector Hub - Suivi Exhaustif de Collection ({len(seed_data)} Éditions)</title>
  <style>
    :root {{
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
    }}

    [data-theme="light"] {{
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
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s, border-color 0.2s;
    }}

    body {{
      font-family: var(--font);
      background-color: var(--bg-main);
      color: var(--text-main);
      line-height: 1.5;
      padding-bottom: 80px;
      min-height: 100vh;
    }}

    .container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Header & Navigation */
    header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
      padding: 16px 0;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }}

    .header-content {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #e11d48, #be123c);
      color: white;
      font-weight: 900;
      font-size: 1.4rem;
      letter-spacing: 1px;
      padding: 6px 14px;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.35);
      border: 2px solid rgba(255,255,255,0.2);
    }}

    .logo-title h1 {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .logo-title p {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 16px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .btn-primary {{
      background: var(--primary);
      color: white;
    }}
    .btn-primary:hover {{
      background: var(--primary-hover);
      transform: translateY(-1px);
    }}

    .btn-secondary {{
      background: transparent;
      border-color: var(--border-color);
      color: var(--text-main);
    }}
    .btn-secondary:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent);
    }}

    /* Dashboard Stats Bar */
    .stats-bar {{
      margin: 24px 0 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
    }}

    .stat-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 16px 20px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--card-shadow);
    }}

    .stat-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--accent);
    }}

    .stat-card.green::before {{ background: var(--success); }}
    .stat-card.amber::before {{ background: var(--warning); }}
    .stat-card.rose::before {{ background: var(--primary); }}
    .stat-card.purple::before {{ background: #a855f7; }}

    .stat-label {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }}

    .stat-value {{
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: baseline;
      gap: 6px;
    }}

    .stat-sub {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: normal;
    }}

    .progress-track {{
      width: 100%;
      height: 6px;
      background: rgba(255,255,255,0.08);
      border-radius: 999px;
      margin-top: 10px;
      overflow: hidden;
    }}

    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--success), #34d399);
      width: 0%;
      transition: width 0.5s ease;
    }}

    /* Filters Section */
    .controls-panel {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .search-row {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .search-input-wrapper {{
      position: relative;
      flex-grow: 1;
      min-width: 260px;
    }}

    .search-input-wrapper span.search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 1rem;
    }}

    .search-input {{
      width: 100%;
      padding: 12px 16px 12px 42px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
    }}
    .search-input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
    }}

    .filter-select {{
      padding: 12px 14px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 0.9rem;
      outline: none;
      cursor: pointer;
      min-width: 160px;
    }}
    .filter-select:focus {{
      border-color: var(--accent);
    }}

    .view-toggle {{
      display: flex;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: hidden;
      background: var(--bg-main);
    }}

    .view-toggle-btn {{
      padding: 10px 14px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.85rem;
      font-weight: 600;
    }}

    .view-toggle-btn.active {{
      background: var(--accent);
      color: #000;
    }}

    /* Pills filter rows */
    .pills-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }}

    .pills-label {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-right: 4px;
    }}

    .pill {{
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 600;
      background: var(--bg-main);
      color: var(--text-muted);
      border: 1px solid var(--border-color);
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }}

    .pill:hover {{
      color: var(--text-main);
      border-color: var(--accent);
    }}

    .pill.active {{
      background: var(--accent);
      color: #0b0f19;
      border-color: var(--accent);
      font-weight: 700;
    }}

    /* CARDS GRID VIEW */
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 22px;
    }}

    .edition-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      position: relative;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }}

    .edition-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--box-shadow);
      border-color: rgba(56, 189, 248, 0.4);
    }}

    /* PHYSICAL BOX COVER PRESENTATION */
    .box-cover-wrapper {{
      width: 100%;
      height: 230px;
      background: #060911;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      cursor: pointer;
      border-bottom: 1px solid var(--border-color);
    }}

    .box-cover-image {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      padding: 10px;
      transition: transform 0.3s ease;
      filter: drop-shadow(0 8px 12px rgba(0,0,0,0.6));
    }}

    .box-cover-wrapper:hover .box-cover-image {{
      transform: scale(1.05);
    }}

    .missing-cover-box {{
      width: 88%;
      height: 75%;
      border: 2px dashed rgba(255,255,255,0.18);
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 8px;
      color: var(--text-muted);
      text-align: center;
      padding: 12px;
      background: rgba(255,255,255,0.02);
      transition: all 0.2s ease;
    }}

    .box-cover-wrapper:hover .missing-cover-box {{
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.05);
      color: var(--accent);
    }}

    .missing-icon {{
      font-size: 2rem;
      opacity: 0.7;
    }}

    .missing-title {{
      font-size: 0.85rem;
      font-weight: 700;
      line-height: 1.2;
    }}

    .missing-sub {{
      font-size: 0.72rem;
      opacity: 0.8;
    }}

    /* Status Ribbon Badge */
    .status-ribbon {{
      position: absolute;
      top: 10px;
      right: 10px;
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      backdrop-filter: blur(8px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.4);
      z-index: 5;
    }}

    .status-ribbon.owned {{
      background: rgba(16, 185, 129, 0.9);
      color: white;
      border: 1px solid rgba(255,255,255,0.3);
    }}

    .status-ribbon.wishlist {{
      background: rgba(245, 158, 11, 0.9);
      color: #111;
      border: 1px solid rgba(255,255,255,0.3);
    }}

    .status-ribbon.none {{
      background: rgba(15, 23, 42, 0.8);
      color: var(--text-muted);
      border: 1px solid rgba(255,255,255,0.15);
    }}

    .verified-badge {{
      position: absolute;
      bottom: 8px;
      left: 10px;
      background: rgba(16, 185, 129, 0.85);
      color: white;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      backdrop-filter: blur(4px);
      display: flex;
      align-items: center;
      gap: 4px;
      z-index: 4;
    }}

    /* Card Content Area */
    .card-body {{
      padding: 16px 18px 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex-grow: 1;
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
    }}

    .card-category {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 3px 8px;
      border-radius: 4px;
      background: var(--tag-bg);
      color: var(--accent);
      display: inline-block;
    }}

    .card-year {{
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
    }}

    .card-meta {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .card-meta span {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}

    .card-description {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.45;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      flex-grow: 1;
    }}

    .card-user-info {{
      background: rgba(0,0,0,0.25);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 8px 10px;
      font-size: 0.78rem;
      display: flex;
      flex-direction: column;
      gap: 4px;
      color: var(--text-muted);
    }}

    .card-user-info strong {{
      color: var(--text-main);
    }}

    .card-footer {{
      display: flex;
      gap: 8px;
      margin-top: auto;
      padding-top: 12px;
      border-top: 1px solid var(--border-color);
    }}

    .status-select-btn {{
      flex-grow: 1;
      padding: 7px 10px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      font-size: 0.8rem;
      font-weight: 600;
      background: var(--bg-main);
      color: var(--text-main);
      cursor: pointer;
      text-align: center;
    }}
    .status-select-btn:hover {{
      border-color: var(--accent);
    }}

    .edit-btn {{
      padding: 7px 11px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.85rem;
    }}
    .edit-btn:hover {{
      color: var(--accent);
      border-color: var(--accent);
    }}

    .google-btn {{
      padding: 7px 10px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.78rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .google-btn:hover {{
      color: #fbbf24;
      border-color: #fbbf24;
    }}

    /* TABLE VIEW */
    .table-container {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      overflow-x: auto;
      box-shadow: var(--card-shadow);
      display: none;
    }}

    table.editions-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      text-align: left;
    }}

    table.editions-table th {{
      background: var(--bg-surface);
      color: var(--text-muted);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 12px 16px;
      border-bottom: 2px solid var(--border-color);
    }}

    table.editions-table td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
    }}

    table.editions-table tr:hover td {{
      background: var(--bg-card-hover);
    }}

    .table-thumb {{
      width: 48px;
      height: 48px;
      object-fit: contain;
      border-radius: 4px;
      background: #000;
      border: 1px solid var(--border-color);
      cursor: pointer;
    }}

    /* LOAD MORE / PAGINATION */
    .pagination-bar {{
      margin-top: 32px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }}

    .load-more-btn {{
      padding: 14px 28px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      border-radius: 10px;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      box-shadow: var(--card-shadow);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .load-more-btn:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent);
      color: var(--accent);
      transform: translateY(-2px);
    }}

    .pagination-info {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    /* LIGHTBOX MODAL */
    .modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease;
      padding: 20px;
    }}

    .modal-backdrop.open {{
      opacity: 1;
      visibility: visible;
    }}

    .modal-window {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      max-width: 850px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8);
      position: relative;
      display: flex;
      flex-direction: column;
    }}

    .modal-header {{
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-header h2 {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-main);
    }}

    .modal-close-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
      line-height: 1;
    }}
    .modal-close-btn:hover {{
      color: var(--primary);
    }}

    .modal-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* Lightbox specific */
    .lightbox-image-container {{
      width: 100%;
      max-height: 480px;
      background: #050811;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: 16px;
    }}

    .lightbox-image {{
      max-width: 100%;
      max-height: 440px;
      object-fit: contain;
      filter: drop-shadow(0 12px 24px rgba(0,0,0,0.8));
    }}

    /* Form Fields */
    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .form-group label {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .form-control {{
      padding: 10px 12px;
      background: var(--bg-main);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: var(--text-main);
      font-size: 0.9rem;
      outline: none;
    }}
    .form-control:focus {{
      border-color: var(--accent);
    }}

    .form-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}

    .modal-footer {{
      padding: 16px 24px;
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: flex-end;
      gap: 12px;
    }}

    /* Image dropzone */
    .image-dropzone {{
      border: 2px dashed var(--border-color);
      border-radius: 8px;
      padding: 18px;
      text-align: center;
      cursor: pointer;
      background: var(--bg-main);
      transition: all 0.2s;
    }}
    .image-dropzone:hover {{
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.05);
    }}

    /* Toast */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--success);
      color: white;
      padding: 12px 20px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      box-shadow: 0 10px 15px -3px rgba(0,0,0,0.4);
      z-index: 2000;
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.3s, transform 0.3s;
      pointer-events: none;
    }}
    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Empty state */
    .empty-state {{
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
      display: none;
    }}

    .empty-state span {{
      font-size: 3rem;
      display: block;
      margin-bottom: 12px;
    }}

    @media (max-width: 768px) {{
      .form-row {{
        grid-template-columns: 1fr;
      }}
      .stats-bar {{
        grid-template-columns: 1fr 1fr;
      }}
      .header-content {{
        flex-direction: column;
        align-items: stretch;
      }}
    }}

    /* Box Scanner Styles */
    .scanner-dropzone {{
      border: 2px dashed var(--accent);
      border-radius: 12px;
      padding: 24px;
      text-align: center;
      background: rgba(56, 189, 248, 0.03);
      cursor: pointer;
      position: relative;
      transition: all 0.25s;
    }}
    .scanner-dropzone:hover {{
      background: rgba(56, 189, 248, 0.08);
      border-color: #38bdf8;
    }}
    .scanner-laser-overlay {{
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.7);
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      z-index: 5;
    }}
    .scanner-laser-line {{
      position: absolute;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, transparent, #38bdf8, #818cf8, #38bdf8, transparent);
      box-shadow: 0 0 16px #38bdf8;
      top: 10%;
      animation: laserSweep 1.6s infinite ease-in-out alternate;
    }}
    @keyframes laserSweep {{
      0% {{ top: 8%; }}
      100% {{ top: 88%; }}
    }}
    .scanner-status-text {{
      color: #fff;
      font-weight: 700;
      font-size: 0.9rem;
      background: rgba(0,0,0,0.8);
      padding: 8px 18px;
      border-radius: 20px;
      border: 1px solid rgba(56,189,248,0.5);
      letter-spacing: 0.5px;
    }}
    .candidate-card {{
      display: flex;
      gap: 14px;
      align-items: center;
      padding: 10px 14px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      margin-bottom: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .candidate-card:hover {{
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.05);
      transform: translateX(3px);
    }}
    .candidate-card.selected {{
      border-color: #10b981;
      background: rgba(16, 185, 129, 0.08);
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="container header-content">
      <div class="logo-area">
        <div class="logo-badge">MONOPOLY</div>
        <div class="logo-title">
          <h1>Collector Hub <span>🎩</span></h1>
          <p>Répertoire Mondial & Suivi de Collection ({len(seed_data)} Éditions répertoriées)</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="btn btn-secondary" id="themeBtn" title="Basculer Mode Clair / Sombre">🌓 Thème</button>
        <button class="btn btn-secondary" id="exportCsvBtn" title="Exporter pour Microsoft Excel">📊 Export Excel (CSV)</button>
        <button class="btn btn-secondary" id="backupJsonBtn" title="Sauvegarder ma progression">💾 Sauvegarde</button>
        <label class="btn btn-secondary" style="cursor:pointer;" title="Restaurer une sauvegarde">
          📥 Restaurer <input type="file" id="importJsonInput" accept=".json" style="display:none;">
        </label>
        <button class="btn btn-secondary" id="scanBoxBtn" style="background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; font-weight: 700; border: none; box-shadow: 0 4px 12px rgba(99,102,241,0.35);" title="Identifier une boîte par photo ou code-barres">📸 Scanner & Identifier</button>
        <button class="btn btn-primary" id="addCustomBtn">➕ Ajouter manuellement</button>
      </div>
    </div>
  </header>

  <main class="container">
    <!-- Stats Dashboard -->
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label">Éditions Répertoriées</div>
        <div class="stat-value" id="statTotal">{len(seed_data)}</div>
        <div class="stat-sub">Base mondiale exhaustive</div>
      </div>
      <div class="stat-card purple">
        <div class="stat-label">Jaquettes Réelles</div>
        <div class="stat-value" id="statWithPhotos">0</div>
        <div class="stat-sub" id="statPhotoPct">Photos physiques vérifiées</div>
      </div>
      <div class="stat-card green">
        <div class="stat-label">En ma possession</div>
        <div class="stat-value">
          <span id="statOwned">0</span>
          <span class="stat-sub" id="statOwnedPct">(0%)</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" id="statProgressBar"></div>
        </div>
      </div>
      <div class="stat-card amber">
        <div class="stat-label">Dans ma Wishlist</div>
        <div class="stat-value" id="statWishlist">0</div>
        <div class="stat-sub">Recherchées activement</div>
      </div>
      <div class="stat-card rose">
        <div class="stat-label">Valeur Estimée</div>
        <div class="stat-value" id="statEstimatedValue">0 €</div>
        <div class="stat-sub">Investi : <span id="statSpentValue">0 €</span></div>
      </div>
    </div>

    <!-- Search & Filter Controls -->
    <div class="controls-panel">
      <!-- Search & Select Row -->
      <div class="search-row">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="searchInput" class="search-input" placeholder="Rechercher une édition (ex: Builder, Glisse, 1935, Zelda, Paris, Pokémon, DBZ, Star Wars...)">
        </div>
        <select id="countrySelect" class="filter-select">
          <option value="all">Tous les Pays / Régions</option>
        </select>
        <select id="publisherSelect" class="filter-select">
          <option value="all">Tous les Éditeurs</option>
        </select>
        <select id="decadeSelect" class="filter-select">
          <option value="all">Toutes les Époques</option>
          <option value="1930s">Années 1930 (Origines & Packaging 1935)</option>
          <option value="1940-1970">1940-1979 (Wartime & Boîtes Blanches)</option>
          <option value="1980s">Années 1980 (50ème Anniversaire...)</option>
          <option value="1990s">Années 1990 (Deluxe, 60ème...)</option>
          <option value="2000s">Années 2000 (Rues de Paris, 70ème...)</option>
          <option value="2010s">Années 2010 (Empire, Gamer, 80ème...)</option>
          <option value="2020s">Années 2020 (Builder, Glisse, 85ème...)</option>
        </select>
        <select id="sortSelect" class="filter-select">
          <option value="name-asc">Nom (A → Z)</option>
          <option value="name-desc">Nom (Z → A)</option>
          <option value="year-desc">Année (Plus récente)</option>
          <option value="year-asc">Année (Plus ancienne)</option>
          <option value="status">Statut (Possédé d'abord)</option>
        </select>
        <div class="view-toggle">
          <button class="view-toggle-btn active" id="cardViewBtn">🃏 Grille</button>
          <button class="view-toggle-btn" id="tableViewBtn">📋 Tableau</button>
        </div>
      </div>

      <!-- Status Pills -->
      <div class="pills-container" id="statusPills">
        <span class="pills-label">Statut :</span>
        <span class="pill active" data-status="all">Tous (<span id="countAll">0</span>)</span>
        <span class="pill" data-status="owned">🟢 Possédés (<span id="countOwned">0</span>)</span>
        <span class="pill" data-status="wishlist">⭐ Recherchés (<span id="countWishlist">0</span>)</span>
        <span class="pill" data-status="none">⚪ Non possédés (<span id="countNone">0</span>)</span>
        <span class="pill" data-status="photos-only">📸 Avec Photo Uniquement</span>
      </div>

      <!-- Category Pills -->
      <div class="pills-container" id="categoryPills">
        <span class="pills-label">Catégorie :</span>
        <span class="pill active" data-category="all">Toutes</span>
      </div>
    </div>

    <!-- Empty State Message -->
    <div class="empty-state" id="emptyState">
      <span>🔎</span>
      <h3>Aucune édition ne correspond à vos critères</h3>
      <p>Essayez de réinitialiser la recherche ou de changer les filtres.</p>
    </div>

    <!-- Cards Grid View -->
    <div class="cards-grid" id="cardsContainer"></div>

    <!-- Table View -->
    <div class="table-container" id="tableContainer">
      <table class="editions-table">
        <thead>
          <tr>
            <th style="width: 70px;">Visuel</th>
            <th style="width: 140px;">Statut</th>
            <th>Nom de l'Édition</th>
            <th>Catégorie</th>
            <th>Année</th>
            <th>Éditeur</th>
            <th>Pays</th>
            <th style="width: 110px;">Actions</th>
          </tr>
        </thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>

    <!-- Pagination / Load More Bar -->
    <div class="pagination-bar" id="paginationBar">
      <button class="load-more-btn" id="loadMoreBtn">
        <span>Afficher les 60 éditions suivantes</span> ⬇️
      </button>
      <div class="pagination-info" id="paginationInfo">Affichage de 60 sur 1 189 éditions</div>
    </div>
  </main>

  <!-- LIGHTBOX MODAL -->
  <div class="modal-backdrop" id="lightboxModalBackdrop">
    <div class="modal-window">
      <div class="modal-header">
        <h2 id="lightboxTitle">Aperçu de la Boîte</h2>
        <button class="modal-close-btn" id="closeLightbox">&times;</button>
      </div>
      <div class="modal-body">
        <div class="lightbox-image-container" id="lightboxContainer">
          <img src="" alt="" class="lightbox-image" id="lightboxImg">
        </div>
        <div id="lightboxDetails" style="font-size:0.9rem; line-height:1.6;"></div>
      </div>
      <div class="modal-footer">
        <a href="#" target="_blank" class="btn btn-secondary" id="lightboxGoogleLink">🔍 Google Images</a>
        <button class="btn btn-primary" id="lightboxEditBtn">✏️ Modifier la fiche ou la photo</button>
      </div>
    </div>
  </div>

  <!-- EDIT / DETAILS MODAL -->
  <div class="modal-backdrop" id="editModalBackdrop">
    <div class="modal-window">
      <div class="modal-header">
        <h2 id="modalTitle">Fiche Édition & Ma Boîte</h2>
        <button class="modal-close-btn" id="closeEditModal">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="editItemId">
        <div class="form-row">
          <div class="form-group">
            <label>Statut de possession</label>
            <select id="editStatus" class="form-control">
              <option value="none">Non possédé</option>
              <option value="owned">🟢 Possédé (Dans ma collection)</option>
              <option value="wishlist">⭐ Recherché (Wishlist)</option>
            </select>
          </div>
          <div class="form-group">
            <label>État de l'exemplaire</label>
            <input type="text" id="editCondition" class="form-control" placeholder="ex: Neuf sous blister, Très bon état, Boîte usée">
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Prix d'achat (€)</label>
            <input type="number" step="0.5" id="editPrice" class="form-control" placeholder="ex: 25.00">
          </div>
          <div class="form-group">
            <label>Valeur estimée (€)</label>
            <input type="number" step="0.5" id="editValue" class="form-control" placeholder="ex: 45.00">
          </div>
        </div>

        <div class="form-group">
          <label>Emplacement de rangement</label>
          <input type="text" id="editLocation" class="form-control" placeholder="ex: Étagère Salon A3, Carton Monopoly Vintage">
        </div>

        <div class="form-group">
          <label>Notes personnelles & Détails de ma boîte</label>
          <textarea id="editNotes" class="form-control" rows="2" placeholder="Détails spécifiques (pions manquants, version française, édition limitée numérotée...)"></textarea>
        </div>

        <div class="form-group">
          <label>Photo de la jaquette de votre boîte</label>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="editImageUrl" class="form-control" style="flex-grow:1;" placeholder="Chemin local (images/...) ou URL d'image">
            <button type="button" class="btn btn-secondary" id="clearImageBtn">Supprimer</button>
          </div>
          <div class="image-dropzone" onclick="document.getElementById('editImageFileInput').click();" style="margin-top:8px;">
            <span>📸 Cliquer pour charger une photo depuis votre smartphone ou ordinateur</span>
            <input type="file" id="editImageFileInput" accept="image/*" style="display:none;">
          </div>
        </div>

        <div id="modalImagePreviewContainer" style="max-height:180px; overflow:hidden; border-radius:6px; background:#000; display:flex; align-items:center; justify-content:center;"></div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" id="cancelEditBtn">Annuler</button>
        <button class="btn btn-primary" id="saveEditBtn">Enregistrer les modifications</button>
      </div>
    </div>
  </div>

  <!-- ADD CUSTOM EDITION MODAL -->
  <div class="modal-backdrop" id="addModalBackdrop">
    <div class="modal-window">
      <div class="modal-header">
        <h2>Ajouter une Édition Spécifique</h2>
        <button class="modal-close-btn" id="closeAddModal">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label>Nom de l'édition *</label>
          <input type="text" id="addName" class="form-control" placeholder="ex: Monopoly Super Mario Bros Collector">
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Catégorie</label>
            <input type="text" id="addCategory" list="categoryOptions" class="form-control" placeholder="ex: Jeux Vidéo, Classique...">
            <datalist id="categoryOptions"></datalist>
          </div>
          <div class="form-group">
            <label>Année d'édition</label>
            <input type="number" id="addYear" class="form-control" placeholder="ex: 2021">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Pays / Région</label>
            <input type="text" id="addCountry" class="form-control" placeholder="ex: France">
          </div>
          <div class="form-group">
            <label>Éditeur</label>
            <input type="text" id="addPublisher" class="form-control" placeholder="ex: Hasbro / Winning Moves">
          </div>
        </div>
        <div class="form-group">
          <label>Description & Spécificités</label>
          <textarea id="addDescription" class="form-control" rows="2" placeholder="Description des pions, packaging, règles..."></textarea>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Statut initial</label>
            <select id="addStatus" class="form-control">
              <option value="owned">🟢 Possédé</option>
              <option value="wishlist">⭐ Recherché</option>
              <option value="none">⚪ Non possédé</option>
            </select>
          </div>
          <div class="form-group">
            <label>URL ou Photo de la boîte</label>
            <input type="text" id="addImageUrl" class="form-control" placeholder="images/ma_boite.jpg ou URL">
          </div>
        </div>
        <div class="image-dropzone" onclick="document.getElementById('addImageFileInput').click();">
          <span>📸 Importer une photo de la boîte</span>
          <input type="file" id="addImageFileInput" accept="image/*" style="display:none;">
        </div>
        <div id="addModalImagePreview" style="max-height:140px; overflow:hidden; border-radius:6px; background:#000; display:flex; align-items:center; justify-content:center;"></div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" id="cancelAddBtn">Annuler</button>
        <button class="btn btn-primary" id="confirmAddBtn">Créer l'édition</button>
      </div>
    </div>
  </div>

  <!-- Box Scanner & Identifier Modal -->
  <div class="modal-backdrop" id="scannerModalBackdrop">
    <div class="modal-card" style="max-width: 860px;">
      <div class="modal-header" style="background: linear-gradient(135deg, #1e1b4b, #312e81); color: #fff;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <span style="font-size: 1.6rem;">🔍</span>
          <div>
            <h2 style="font-size: 1.25rem; font-weight: 800; color: #fff; margin: 0;">Scanner & Identifier une Boîte</h2>
            <p style="font-size: 0.8rem; color: #c7d2fe; margin: 2px 0 0 0;">Analyse instantanée par photo, code-barres et reconnaissance intelligente</p>
          </div>
        </div>
        <button class="modal-close-btn" id="closeScannerModal" style="color:#c7d2fe;">&times;</button>
      </div>

      <div class="modal-body" style="max-height: calc(85vh - 130px); overflow-y: auto;">
        <!-- Drag & Drop Zone -->
        <div class="scanner-dropzone" id="scannerDropzone">
          <input type="file" id="scannerFileInput" accept="image/*" style="display:none;" capture="environment">
          <div id="scannerEmptyState">
            <span style="font-size: 2.8rem; display: block; margin-bottom: 8px;">📸</span>
            <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 4px;">Glissez-déposez la photo de votre boîte ici</div>
            <div style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">Face avant ou dos avec code-barres (ordinateur ou smartphone)</div>
            <button class="btn btn-primary" type="button" id="scannerPickFileBtn" style="background: linear-gradient(135deg, #6366f1, #4f46e5); border: none;">Choisir une photo</button>
          </div>
          <div id="scannerPreviewArea" style="display: none; position: relative; text-align: center;">
            <img id="scannerPreviewImg" style="max-height: 230px; max-width: 100%; border-radius: 8px; object-fit: contain; box-shadow: 0 6px 16px rgba(0,0,0,0.5);">
            <div id="scannerScanningOverlay" class="scanner-laser-overlay" style="display: none;">
              <div class="scanner-laser-line"></div>
              <div class="scanner-status-text">⚡ Analyse et identification en cours...</div>
            </div>
            <button class="btn btn-secondary" id="scannerChangePhotoBtn" type="button" style="position: absolute; top: 8px; right: 8px; padding: 5px 12px; font-size: 0.78rem; background: rgba(0,0,0,0.75); color: #fff; border: 1px solid rgba(255,255,255,0.2);">Changer la photo</button>
          </div>
        </div>

        <!-- AI Key Settings Bar (Optional) -->
        <div style="margin-top: 12px; display: flex; align-items: center; justify-content: space-between; background: rgba(255,255,255,0.03); padding: 8px 14px; border-radius: 8px; border: 1px solid var(--border-color); font-size: 0.82rem;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span>🤖 Moteur de détection :</span>
            <span id="aiKeyStatusBadge" style="font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.15); color: #10b981; font-weight: 700;">Code-barres & Catalogue local actif</span>
          </div>
          <button type="button" id="toggleAiKeyBtn" style="background: none; border: none; color: var(--accent); cursor: pointer; text-decoration: underline; font-size: 0.8rem;">Clé IA Gemini (Optionnel)</button>
        </div>
        <div id="aiKeyConfigRow" style="display: none; margin-top: 8px; padding: 12px; background: var(--bg-surface); border-radius: 8px; border: 1px solid var(--border-color);">
          <label style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 4px;">Clé API Google Gemini (Vision automatique) :</label>
          <div style="display: flex; gap: 8px;">
            <input type="password" id="geminiApiKeyInput" class="form-control" placeholder="Collez votre clé API Gemini ici..." style="font-size: 0.85rem;">
            <button class="btn btn-primary" id="saveGeminiApiKeyBtn" type="button" style="padding: 6px 14px; font-size: 0.8rem;">Enregistrer</button>
          </div>
          <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 4px;">Gratuit sur Google AI Studio. Permet la détection automatique même sur les photos floues ou partielles.</div>
        </div>

        <!-- Real-time Assist Bar -->
        <div style="margin-top: 14px;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
            <label style="font-size: 0.78rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Mots-clés / Titre détecté sur la boîte :</label>
            <span id="matchStatsLabel" style="font-size: 0.75rem; color: var(--text-muted);">Recherche dans 1 225 références</span>
          </div>
          <div style="position: relative;">
            <input type="text" id="scannerSearchQuery" class="form-control" placeholder="Titre ou mots visibles sur la boîte (ex: Fortnite, Builder, Gliss, Mega, 1992...)" style="padding-left: 36px; font-weight: 600;">
            <span style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); opacity: 0.5;">🔍</span>
          </div>
        </div>

        <!-- Dynamic Results Container -->
        <div id="scannerResultArea" style="margin-top: 16px;">
          <div style="text-align: center; padding: 24px; color: var(--text-muted); border: 1px dashed var(--border-color); border-radius: 8px;">
            <span>💡</span> Déposez une photo ci-dessus ou saisissez un mot-clé pour lancer l'identification.
          </div>
        </div>
      </div>

      <div class="modal-footer" style="background: var(--bg-surface);">
        <button class="btn btn-secondary" id="closeScannerFooterBtn">Fermer</button>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">Données enregistrées</div>

  <script>
    const SEED_DATA = {seed_json_str};
    const STORAGE_KEY = "monopoly_collection_db_v8";

    let database = [];
    let currentFilterStatus = "all";
    let currentFilterCategory = "all";
    let currentCountry = "all";
    let currentPublisher = "all";
    let currentDecade = "all";
    let currentSearchTerm = "";
    let currentSort = "name-asc";
    let currentView = "card";
    let activeLightboxId = null;

    // Pagination
    const PAGE_SIZE = 60;
    let displayedCount = PAGE_SIZE;

    function handleImageError(img) {{
      img.style.display = "none";
      const fallback = img.nextElementSibling;
      if (fallback) fallback.style.display = "flex";
      const badge = img.parentElement.querySelector(".verified-badge");
      if (badge) badge.style.display = "none";
    }}

    function initDatabase() {{
      let saved = localStorage.getItem(STORAGE_KEY);
      if (!saved) saved = localStorage.getItem("monopoly_collection_db_v7");
      if (!saved) saved = localStorage.getItem("monopoly_collection_db_v6");
      if (!saved) saved = localStorage.getItem("monopoly_collection_db_v5");

      if (saved) {{
        try {{
          const parsed = JSON.parse(saved);
          if (Array.isArray(parsed) && parsed.length > 0) {{
            const savedMap = {{}};
            parsed.forEach(function(item) {{
              if (item && item.id) savedMap[item.id] = item;
              if (item && item.name) savedMap[item.name.toLowerCase().trim()] = item;
            }});

            const reconciled = SEED_DATA.map(function(seedItem) {{
              const userItem = savedMap[seedItem.id] || savedMap[seedItem.name.toLowerCase().trim()];
              const base = Object.assign({{
                status: "none",
                condition: "",
                price: "",
                value: "",
                location: "",
                notes: ""
              }}, seedItem);

              if (userItem) {{
                const finalStatus = (seedItem.status === "owned") ? "owned" : (userItem.status || "none");
                const imageUrl = (seedItem.image_url && seedItem.is_verified_box)
                  ? seedItem.image_url
                  : (userItem.image_url && !userItem.image_url.startsWith("data:image/svg") ? userItem.image_url : (seedItem.image_url || ""));
                
                return Object.assign({{}}, base, userItem, {{
                  status: finalStatus,
                  image_url: imageUrl,
                  back_image_url: seedItem.back_image_url || userItem.back_image_url || "",
                  is_verified_box: Boolean(seedItem.is_verified_box || userItem.is_verified_box),
                  condition: seedItem.condition || userItem.condition || "",
                  location: seedItem.location || userItem.location || "",
                  notes: seedItem.notes || userItem.notes || ""
                }});
              }}
              return base;
            }});

            // Preserve any custom user-created editions
            parsed.forEach(function(userItem) {{
              if (userItem && userItem.id && userItem.id.startsWith("custom-")) {{
                reconciled.push(userItem);
              }}
            }});

            database = reconciled;
            saveDatabase();
            return;
          }}
        }} catch(e) {{}}
      }}
      loadFromSeed();
    }}

    function loadFromSeed() {{
      database = SEED_DATA.map(function(item) {{
        return Object.assign({{
          status: "none",
          condition: "",
          price: "",
          value: "",
          location: "",
          notes: ""
        }}, item);
      }});
      saveDatabase();
    }}

    function saveDatabase() {{
      localStorage.setItem(STORAGE_KEY, JSON.stringify(database));
      renderStats();
      populateFilters();
    }}

    function showToast(msg) {{
      const toast = document.getElementById("toast");
      toast.textContent = msg;
      toast.classList.add("show");
      setTimeout(function() {{
        toast.classList.remove("show");
      }}, 2600);
    }}

    function renderStats() {{
      const total = database.length;
      const owned = database.filter(function(e) {{ return e.status === "owned"; }}).length;
      const wishlist = database.filter(function(e) {{ return e.status === "wishlist"; }}).length;
      const none = database.filter(function(e) {{ return e.status === "none" || !e.status; }}).length;
      const withPhotos = database.filter(function(e) {{ return Boolean(e.image_url); }}).length;

      let totalVal = 0;
      let totalSpent = 0;
      database.forEach(function(e) {{
        if (e.status === "owned") {{
          if (e.value) totalVal += parseFloat(e.value) || 0;
          if (e.price) totalSpent += parseFloat(e.price) || 0;
        }}
      }});

      const pct = total > 0 ? Math.round((owned / total) * 100) : 0;
      const photoPct = total > 0 ? Math.round((withPhotos / total) * 100) : 0;

      document.getElementById("statTotal").textContent = total.toLocaleString("fr-FR");
      document.getElementById("statWithPhotos").textContent = withPhotos.toLocaleString("fr-FR");
      document.getElementById("statPhotoPct").textContent = photoPct + "% de la base en photos";
      document.getElementById("statOwned").textContent = owned.toLocaleString("fr-FR");
      document.getElementById("statOwnedPct").textContent = "(" + pct + "%)";
      document.getElementById("statProgressBar").style.width = pct + "%";
      document.getElementById("statWishlist").textContent = wishlist.toLocaleString("fr-FR");
      document.getElementById("statEstimatedValue").textContent = totalVal.toLocaleString('fr-FR', {{ minimumFractionDigits: 0, maximumFractionDigits: 2 }}) + " €";
      document.getElementById("statSpentValue").textContent = totalSpent.toLocaleString('fr-FR', {{ minimumFractionDigits: 0, maximumFractionDigits: 2 }}) + " €";

      document.getElementById("countAll").textContent = total;
      document.getElementById("countOwned").textContent = owned;
      document.getElementById("countWishlist").textContent = wishlist;
      document.getElementById("countNone").textContent = none;
    }}

    function populateFilters() {{
      // Categories
      const catMap = {{}};
      database.forEach(function(e) {{
        if (e.category) catMap[e.category] = (catMap[e.category] || 0) + 1;
      }});
      const categories = Object.keys(catMap).sort();

      const catContainer = document.getElementById("categoryPills");
      const currentActive = currentFilterCategory;

      catContainer.innerHTML = '<span class="pills-label">Catégorie :</span><span class="pill ' + (currentActive === "all" ? "active" : "") + '" data-category="all">Toutes (' + database.length + ')</span>';
      categories.forEach(function(cat) {{
        const count = catMap[cat];
        const pill = document.createElement("span");
        pill.className = "pill " + (currentActive === cat ? "active" : "");
        pill.dataset.category = cat;
        pill.textContent = cat + " (" + count + ")";
        catContainer.appendChild(pill);
      }});

      const datalist = document.getElementById("categoryOptions");
      datalist.innerHTML = "";
      categories.forEach(function(cat) {{
        const opt = document.createElement("option");
        opt.value = cat;
        datalist.appendChild(opt);
      }});

      // Countries
      const countrySet = {{}};
      database.forEach(function(e) {{
        if (e.country) countrySet[e.country] = true;
      }});
      const countries = Object.keys(countrySet).sort();
      const countrySelect = document.getElementById("countrySelect");
      const selectedVal = countrySelect.value;
      countrySelect.innerHTML = '<option value="all">Tous les Pays / Régions</option>';
      countries.forEach(function(c) {{
        const opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        countrySelect.appendChild(opt);
      }});
      if (countrySet[selectedVal]) countrySelect.value = selectedVal;

      // Publishers
      const pubSet = {{}};
      database.forEach(function(e) {{
        if (e.publisher) pubSet[e.publisher] = true;
      }});
      const pubs = Object.keys(pubSet).sort();
      const pubSelect = document.getElementById("publisherSelect");
      const selectedPub = pubSelect.value;
      pubSelect.innerHTML = '<option value="all">Tous les Éditeurs</option>';
      pubs.forEach(function(p) {{
        const opt = document.createElement("option");
        opt.value = p;
        opt.textContent = p;
        pubSelect.appendChild(opt);
      }});
      if (pubSet[selectedPub]) pubSelect.value = selectedPub;
    }}

    function getFilteredAndSortedEditions() {{
      return database.filter(function(item) {{
        if (currentFilterStatus === "owned" && item.status !== "owned") return false;
        if (currentFilterStatus === "wishlist" && item.status !== "wishlist") return false;
        if (currentFilterStatus === "none" && item.status !== "none" && item.status) return false;
        if (currentFilterStatus === "photos-only" && !item.image_url) return false;

        if (currentFilterCategory !== "all" && item.category !== currentFilterCategory) return false;
        if (currentCountry !== "all" && item.country !== currentCountry) return false;
        if (currentPublisher !== "all" && item.publisher !== currentPublisher) return false;

        // Decade filter
        if (currentDecade !== "all") {{
          const y = item.year || 0;
          if (currentDecade === "1930s" && (y < 1930 || y > 1939)) return false;
          if (currentDecade === "1940-1970" && (y < 1940 || y > 1979)) return false;
          if (currentDecade === "1980s" && (y < 1980 || y > 1989)) return false;
          if (currentDecade === "1990s" && (y < 1990 || y > 1999)) return false;
          if (currentDecade === "2000s" && (y < 2000 || y > 2009)) return false;
          if (currentDecade === "2010s" && (y < 2010 || y > 2019)) return false;
          if (currentDecade === "2020s" && y < 2020) return false;
        }}

        if (currentSearchTerm) {{
          const term = currentSearchTerm.toLowerCase();
          const matchName = item.name && item.name.toLowerCase().includes(term);
          const matchDesc = item.description && item.description.toLowerCase().includes(term);
          const matchCat = item.category && item.category.toLowerCase().includes(term);
          const matchCountry = item.country && item.country.toLowerCase().includes(term);
          const matchPub = item.publisher && item.publisher.toLowerCase().includes(term);
          const matchNotes = item.notes && item.notes.toLowerCase().includes(term);
          const matchLoc = item.location && item.location.toLowerCase().includes(term);
          const matchYear = item.year && item.year.toString().includes(term);
          if (!matchName && !matchDesc && !matchCat && !matchCountry && !matchPub && !matchNotes && !matchLoc && !matchYear) {{
            return false;
          }}
        }}
        return true;
      }}).sort(function(a, b) {{
        if (currentSort === "name-asc") return (a.name || "").localeCompare(b.name || "");
        if (currentSort === "name-desc") return (b.name || "").localeCompare(a.name || "");
        if (currentSort === "year-desc") return (b.year || 0) - (a.year || 0);
        if (currentSort === "year-asc") return (a.year || 0) - (b.year || 0);
        if (currentSort === "status") {{
          const order = {{ owned: 1, wishlist: 2, none: 3 }};
          return (order[a.status] || 3) - (order[b.status] || 3);
        }}
        return 0;
      }});
    }}

    function renderList(resetPagination) {{
      if (resetPagination) displayedCount = PAGE_SIZE;

      const filtered = getFilteredAndSortedEditions();
      const cardsContainer = document.getElementById("cardsContainer");
      const tableBody = document.getElementById("tableBody");
      const emptyState = document.getElementById("emptyState");
      const paginationBar = document.getElementById("paginationBar");

      if (filtered.length === 0) {{
        emptyState.style.display = "block";
        cardsContainer.style.display = "none";
        document.getElementById("tableContainer").style.display = "none";
        paginationBar.style.display = "none";
        return;
      }}

      emptyState.style.display = "none";

      const sliceToDisplay = filtered.slice(0, displayedCount);

      if (currentView === "card") {{
        cardsContainer.style.display = "grid";
        document.getElementById("tableContainer").style.display = "none";
        renderCards(sliceToDisplay, cardsContainer);
      }} else {{
        cardsContainer.style.display = "none";
        document.getElementById("tableContainer").style.display = "block";
        renderTable(sliceToDisplay, tableBody);
      }}

      // Update pagination controls
      if (filtered.length > displayedCount) {{
        paginationBar.style.display = "flex";
        const remaining = filtered.length - displayedCount;
        const nextBatch = Math.min(PAGE_SIZE, remaining);
        document.getElementById("loadMoreBtn").innerHTML = '<span>Afficher les ' + nextBatch + ' éditions suivantes (' + remaining + ' restantes)</span> ⬇️';
        document.getElementById("paginationInfo").textContent = 'Affichage de ' + sliceToDisplay.length + ' sur ' + filtered.length + ' éditions';
      }} else {{
        paginationBar.style.display = "none";
      }}
    }}

    function renderCards(items, container) {{
      container.innerHTML = "";
      items.forEach(function(item) {{
        const card = document.createElement("div");
        card.className = "edition-card";

        const statusLabel = item.status === "owned" 
          ? "🟢 Possédé" 
          : item.status === "wishlist" 
          ? "⭐ Recherché" 
          : "⚪ Non possédé";

        const badgeClass = item.status === "owned" ? "owned" : item.status === "wishlist" ? "wishlist" : "none";

        const googleQuery = encodeURIComponent(item.name + " boite jeu");
        const googleUrl = "https://www.google.com/search?tbm=isch&q=" + googleQuery;

        let coverHtml = "";
        if (item.image_url) {{
          const verifiedBadge = item.back_image_url
            ? '<div class="verified-badge" style="background:linear-gradient(135deg, #10b981, #059669); font-weight:700;">📸 Recto / Verso</div>'
            : (item.is_verified_box ? '<div class="verified-badge">📸 Photo Réelle</div>' : '');

          coverHtml = 
            '<img class="box-cover-image" src="' + item.image_url + '" alt="' + item.name + '" loading="lazy" onerror="handleImageError(this)">' +
            '<div class="missing-cover-box" style="display:none;">' +
              '<div class="missing-icon">📦</div>' +
              '<div class="missing-title">' + item.name + '</div>' +
              '<div class="missing-sub">Photo locale non trouvée</div>' +
            '</div>' +
            verifiedBadge;
        }} else {{
          coverHtml = 
            '<div class="missing-cover-box">' +
              '<div class="missing-icon">📷</div>' +
              '<div class="missing-title">' + item.name + '</div>' +
              '<div class="missing-sub">Cliquer pour charger la photo de votre boîte</div>' +
            '</div>';
        }}

        let userInfoHtml = "";
        if (item.status === "owned") {{
          userInfoHtml = '<div class="card-user-info">';
          if (item.condition) userInfoHtml += '<div><strong>État:</strong> ' + item.condition + '</div>';
          if (item.location) userInfoHtml += '<div><strong>Emplacement:</strong> ' + item.location + '</div>';
          if (item.price || item.value) {{
            userInfoHtml += '<div>' + (item.price ? 'Achat: ' + item.price + '€ ' : '') + (item.value ? '| Est.: ' + item.value + '€' : '') + '</div>';
          }}
          if (item.notes) userInfoHtml += '<div><strong>Note:</strong> ' + item.notes + '</div>';
          userInfoHtml += '</div>';
        }} else if (item.status === "wishlist" && (item.notes || item.value)) {{
          userInfoHtml = '<div class="card-user-info">';
          if (item.value) userInfoHtml += '<div>Budget max: ' + item.value + '€</div>';
          if (item.notes) userInfoHtml += '<div>' + item.notes + '</div>';
          userInfoHtml += '</div>';
        }}

        card.innerHTML = 
          '<div class="box-cover-wrapper" data-lightbox-id="' + item.id + '" title="Cliquer pour inspecter la jaquette en grand format">' +
            '<div class="status-ribbon ' + badgeClass + '">' + statusLabel + '</div>' +
            coverHtml +
          '</div>' +
          '<div class="card-body">' +
            '<div class="card-top">' +
              '<span class="card-category">' + (item.category || 'Général') + '</span>' +
              '<span class="card-year">' + (item.year || '—') + '</span>' +
            '</div>' +
            '<h3 class="card-title">' + item.name + '</h3>' +
            '<div class="card-meta">' +
              '<span>📍 ' + (item.country || 'Monde') + '</span>' +
              '<span>🏢 ' + (item.publisher || 'Hasbro') + '</span>' +
            '</div>' +
            '<p class="card-description">' + (item.description || '') + '</p>' +
            userInfoHtml +
            '<div class="card-footer">' +
              '<button class="status-select-btn" data-action="cycle" data-id="' + item.id + '">' + statusLabel + '</button>' +
              '<button class="edit-btn" data-id="' + item.id + '" title="Modifier la fiche ou la photo">✏️</button>' +
              '<a href="' + googleUrl + '" target="_blank" class="google-btn" title="Rechercher sur Google Images">🔍 Google</a>' +
            '</div>' +
          '</div>';

        container.appendChild(card);
      }});
    }}

    function renderTable(items, tbody) {{
      tbody.innerHTML = "";
      items.forEach(function(item) {{
        const tr = document.createElement("tr");

        const statusLabel = item.status === "owned" 
          ? "🟢 Possédé" 
          : item.status === "wishlist" 
          ? "⭐ Recherché" 
          : "⚪ Non possédé";

        const badgeClass = item.status === "owned" ? "owned" : item.status === "wishlist" ? "wishlist" : "none";

        let thumbHtml = "";
        if (item.image_url) {{
          thumbHtml = '<img src="' + item.image_url + '" class="table-thumb" data-lightbox-id="' + item.id + '" loading="lazy" onerror="this.remove()">';
        }} else {{
          thumbHtml = '<div class="table-thumb" data-lightbox-id="' + item.id + '" style="display:flex;align-items:center;justify-content:center;font-size:1.1rem;">📷</div>';
        }}

        tr.innerHTML = 
          '<td>' + thumbHtml + '</td>' +
          '<td><span class="status-ribbon ' + badgeClass + '" style="position:static;display:inline-block;cursor:pointer;" data-action="cycle" data-id="' + item.id + '">' + statusLabel + '</span></td>' +
          '<td><strong>' + item.name + '</strong></td>' +
          '<td><span class="card-category">' + (item.category || '') + '</span></td>' +
          '<td>' + (item.year || '—') + '</td>' +
          '<td>' + (item.publisher || 'Hasbro') + '</td>' +
          '<td>' + (item.country || 'Monde') + '</td>' +
          '<td><button class="edit-btn" data-id="' + item.id + '" style="padding:4px 8px;">✏️ Modifier</button></td>';

        tbody.appendChild(tr);
      }});
    }}

    function cycleStatus(id) {{
      const item = database.find(function(e) {{ return e.id === id; }});
      if (!item) return;
      if (item.status === "none" || !item.status) {{
        item.status = "owned";
        showToast('"' + item.name + '" marqué comme POSSÉDÉ !');
      }} else if (item.status === "owned") {{
        item.status = "wishlist";
        showToast('"' + item.name + '" ajouté à votre WISHLIST !');
      }} else {{
        item.status = "none";
        showToast('"' + item.name + '" retiré de la collection.');
      }}
      saveDatabase();
      renderList(false);
    }}

    // Lightbox Modal
    function openLightbox(id) {{
      const item = database.find(function(e) {{ return e.id === id; }});
      if (!item) return;
      activeLightboxId = id;

      document.getElementById("lightboxTitle").textContent = item.name + " (" + (item.year || 'Année inconnue') + ")";
      const img = document.getElementById("lightboxImg");
      const container = document.getElementById("lightboxContainer");

      if (item.image_url && item.back_image_url) {{
        img.style.display = "none";
        container.innerHTML = 
          '<div style="display:flex; gap:20px; justify-content:center; align-items:flex-start; flex-wrap:wrap; max-height:480px; overflow-y:auto; width:100%; padding:8px;">' +
            '<div style="text-align:center; flex:1; min-width:260px; max-width:440px;">' +
              '<span style="font-size:0.8rem; font-weight:700; color:var(--primary); display:block; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">📸 Face Avant (Votre boîte)</span>' +
              '<img src="' + item.image_url + '" style="max-height:400px; width:auto; max-width:100%; object-fit:contain; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.6); border:2px solid var(--border);">' +
            '</div>' +
            '<div style="text-align:center; flex:1; min-width:260px; max-width:440px;">' +
              '<span style="font-size:0.8rem; font-weight:700; color:#10b981; display:block; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">📦 Dos de la Boîte (Pions & Contenu)</span>' +
              '<img src="' + item.back_image_url + '" style="max-height:400px; width:auto; max-width:100%; object-fit:contain; border-radius:8px; box-shadow:0 8px 24px rgba(0,0,0,0.6); border:2px solid var(--border);">' +
            '</div>' +
          '</div>';
      }} else if (item.image_url) {{
        img.style.display = "block";
        img.src = item.image_url;
      }} else {{
        img.style.display = "none";
        container.innerHTML = '<div style="color:var(--text-muted); text-align:center; padding:40px;"><span style="font-size:3rem;">📷</span><p>Aucune jaquette enregistrée pour le moment.<br>Cliquez sur &quot;Modifier&quot; pour en ajouter une.</p></div>';
      }}

      let detailsHtml = '<p><strong>Catégorie :</strong> ' + (item.category || 'Standard') + ' | <strong>Éditeur :</strong> ' + (item.publisher || 'Hasbro') + ' | <strong>Pays :</strong> ' + (item.country || 'Monde') + '</p>';
      if (item.description) detailsHtml += '<p style="margin-top:8px; color:var(--text-muted);">' + item.description + '</p>';

      if (item.status === "owned") {{
        detailsHtml += '<div style="margin-top:12px; padding:12px; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.35); border-radius:6px; color:#10b981;">';
        detailsHtml += '<div style="font-weight:700; margin-bottom:4px;">🟢 Exemplaire dans votre collection</div>';
        detailsHtml += (item.condition ? '<div><strong>État :</strong> ' + item.condition + '</div>' : '');
        detailsHtml += (item.location ? '<div><strong>Emplacement :</strong> ' + item.location + '</div>' : '');
        if (item.notes) detailsHtml += '<div style="margin-top:4px; font-size:0.85rem; color:#d1fae5;"><strong>Notes & Réf :</strong> ' + item.notes + '</div>';
        detailsHtml += '</div>';
      }}

      document.getElementById("lightboxDetails").innerHTML = detailsHtml;

      const googleQuery = encodeURIComponent(item.name + " boîte monopoly");
      document.getElementById("lightboxGoogleLink").href = "https://www.google.com/search?tbm=isch&q=" + googleQuery;

      document.getElementById("lightboxModalBackdrop").classList.add("open");
    }}

    // Edit Modal
    function openEditModal(id) {{
      const item = database.find(function(e) {{ return e.id === id; }});
      if (!item) return;

      document.getElementById("modalTitle").textContent = "Fiche : " + item.name;
      document.getElementById("editItemId").value = item.id;
      document.getElementById("editStatus").value = item.status || "none";
      document.getElementById("editCondition").value = item.condition || "";
      document.getElementById("editPrice").value = item.price || "";
      document.getElementById("editValue").value = item.value || "";
      document.getElementById("editLocation").value = item.location || "";
      document.getElementById("editNotes").value = item.notes || "";
      document.getElementById("editImageUrl").value = item.image_url || "";

      updateEditPreview(item);
      document.getElementById("editModalBackdrop").classList.add("open");
    }}

    function updateEditPreview(item) {{
      const preview = document.getElementById("modalImagePreviewContainer");
      const url = document.getElementById("editImageUrl").value.trim();
      if (url) {{
        preview.innerHTML = '<img src="' + url + '" style="max-height:160px; max-width:100%; object-fit:contain; border-radius:4px;" onerror="this.remove()">';
      }} else {{
        preview.innerHTML = '<div style="padding:20px; color:var(--text-muted); font-size:0.85rem;">Aucune photo sélectionnée</div>';
      }}
    }}

    function saveEditModal() {{
      const id = document.getElementById("editItemId").value;
      const item = database.find(function(e) {{ return e.id === id; }});
      if (!item) return;

      item.status = document.getElementById("editStatus").value;
      item.condition = document.getElementById("editCondition").value.trim();
      item.price = document.getElementById("editPrice").value.trim();
      item.value = document.getElementById("editValue").value.trim();
      item.location = document.getElementById("editLocation").value.trim();
      item.notes = document.getElementById("editNotes").value.trim();
      
      const newImg = document.getElementById("editImageUrl").value.trim();
      item.image_url = newImg;
      item.is_verified_box = Boolean(newImg);

      document.getElementById("editModalBackdrop").classList.remove("open");
      saveDatabase();
      renderList(false);
      showToast('Fiche de "' + item.name + '" mise à jour !');
    }}

    // Add Modal
    function openAddModal() {{
      document.getElementById("addName").value = "";
      document.getElementById("addCategory").value = "";
      document.getElementById("addYear").value = new Date().getFullYear();
      document.getElementById("addCountry").value = "France";
      document.getElementById("addPublisher").value = "Hasbro";
      document.getElementById("addDescription").value = "";
      document.getElementById("addImageUrl").value = "";
      document.getElementById("addStatus").value = "owned";
      document.getElementById("addModalImagePreview").innerHTML = "";
      document.getElementById("addModalBackdrop").classList.add("open");
    }}

    function saveCustomEdition() {{
      const name = document.getElementById("addName").value.trim();
      if (!name) {{
        alert("Veuillez saisir un nom pour l'édition.");
        return;
      }}

      const newEdition = {{
        id: "custom-" + Date.now(),
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
      }};

      database.unshift(newEdition);
      document.getElementById("addModalBackdrop").classList.remove("open");
      saveDatabase();
      renderList(true);
      showToast('Édition "' + name + '" créée avec succès !');
    }}

    // EXPORT & BACKUP
    function exportToCsv() {{
      const headers = ["ID", "Statut", "Nom", "Categorie", "Annee", "Pays", "Editeur", "Image_URL", "Etat", "Prix_Achat_EUR", "Valeur_Estimee_EUR", "Emplacement", "Notes", "Description"];
      const rows = database.map(function(e) {{
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
      }});

      const csvContent = "\\ufeff" + headers.join(";") + "\\n" + rows.map(function(r) {{ return r.join(";"); }}).join("\\n");
      const blob = new Blob([csvContent], {{ type: "text/csv;charset=utf-8;" }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "monopoly_collection_" + new Date().toISOString().slice(0,10) + ".csv";
      a.click();
      URL.revokeObjectURL(url);
      showToast("Fichier CSV exporté pour Excel !");
    }}

    function backupToJson() {{
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(database, null, 2));
      const a = document.createElement("a");
      a.href = dataStr;
      a.download = "monopoly_collection_backup_" + new Date().toISOString().slice(0,10) + ".json";
      a.click();
      showToast("Sauvegarde JSON téléchargée !");
    }}

    function importFromJson(e) {{
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(event) {{
        try {{
          const imported = JSON.parse(event.target.result);
          if (Array.isArray(imported)) {{
            database = imported;
            saveDatabase();
            renderList(true);
            showToast("Collection restaurée avec succès !");
          }} else {{
            alert("Format JSON non valide.");
          }}
        }} catch(err) {{
          alert("Erreur lors de la lecture du fichier : " + err.message);
        }}
      }};
      reader.readAsText(file);
      e.target.value = "";
    }}

    function handleImageUpload(file, inputTargetId, previewContainerId) {{
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        const dataUrl = e.target.result;
        document.getElementById(inputTargetId).value = dataUrl;
        document.getElementById(previewContainerId).innerHTML = '<img src="' + dataUrl + '" style="width:100%; height:100%; object-fit:contain; border-radius:4px;">';
      }};
      reader.readAsDataURL(file);
    }}

    // ==========================================
    // BOX SCANNER & INTELLIGENT IDENTIFIER
    // ==========================================
    let currentScannedDataUrl = "";
    let currentScannerCandidates = [];
    let detectedInfoFromScan = null;

    function openScannerModal() {{
      const modal = document.getElementById("scannerModalBackdrop");
      modal.classList.add("open");
      updateAiBadgeStatus();
      if (!currentScannedDataUrl) {{
        resetScannerUI();
      }}
    }}

    function closeScannerModal() {{
      const modal = document.getElementById("scannerModalBackdrop");
      modal.classList.remove("open");
    }}

    function updateAiBadgeStatus() {{
      const key = localStorage.getItem("gemini_api_key");
      const badge = document.getElementById("aiKeyStatusBadge");
      if (key && key.trim()) {{
        badge.textContent = "✨ IA Gemini Vision Active";
        badge.style.background = "rgba(99, 102, 241, 0.2)";
        badge.style.color = "#818cf8";
        document.getElementById("geminiApiKeyInput").value = key;
      }} else {{
        badge.textContent = "Code-barres & Catalogue local actif";
        badge.style.background = "rgba(16, 185, 129, 0.15)";
        badge.style.color = "#10b981";
      }}
    }}

    function resetScannerUI() {{
      currentScannedDataUrl = "";
      currentScannerCandidates = [];
      detectedInfoFromScan = null;
      document.getElementById("scannerEmptyState").style.display = "block";
      document.getElementById("scannerPreviewArea").style.display = "none";
      document.getElementById("scannerPreviewImg").src = "";
      document.getElementById("scannerScanningOverlay").style.display = "none";
      document.getElementById("scannerSearchQuery").value = "";
      document.getElementById("scannerResultArea").innerHTML = 
        '<div style="text-align: center; padding: 24px; color: var(--text-muted); border: 1px dashed var(--border-color); border-radius: 8px;">' +
        '<span>💡</span> Déposez une photo ci-dessus ou saisissez un mot-clé pour lancer l\\'identification.' +
        '</div>';
      document.getElementById("matchStatsLabel").textContent = "Recherche dans " + database.length + " références";
    }}

    function handleScannerFile(file) {{
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        currentScannedDataUrl = e.target.result;
        document.getElementById("scannerEmptyState").style.display = "none";
        const previewArea = document.getElementById("scannerPreviewArea");
        const previewImg = document.getElementById("scannerPreviewImg");
        const overlay = document.getElementById("scannerScanningOverlay");
        previewImg.src = currentScannedDataUrl;
        previewArea.style.display = "block";
        overlay.style.display = "flex";

        setTimeout(function() {{
          analyzeUploadedBox(currentScannedDataUrl, file.name);
        }}, 600);
      }};
      reader.readAsDataURL(file);
    }}

    async function analyzeUploadedBox(dataUrl, fileName) {{
      const overlay = document.getElementById("scannerScanningOverlay");
      let detectedBarcode = null;
      let aiDetection = null;

      // 1. Barcode detector API if available
      if ("BarcodeDetector" in window) {{
        try {{
          const barcodeDetector = new BarcodeDetector({{
            formats: ["ean_13", "ean_8", "upc_a", "upc_e", "code_128"]
          }});
          const img = document.getElementById("scannerPreviewImg");
          const barcodes = await barcodeDetector.detect(img);
          if (barcodes && barcodes.length > 0) {{
            detectedBarcode = barcodes[0].rawValue;
          }}
        }} catch(err) {{
          console.log("Barcode detection:", err);
        }}
      }}

      // 2. Optional Gemini Vision
      const geminiKey = localStorage.getItem("gemini_api_key");
      if (geminiKey && geminiKey.trim()) {{
        try {{
          const base64Data = dataUrl.split(",")[1];
          const mimeType = dataUrl.substring(dataUrl.indexOf(":") + 1, dataUrl.indexOf(";"));
          const response = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + geminiKey.trim(), {{
            method: "POST",
            headers: {{ "Content-Type": "application/json" }},
            body: JSON.stringify({{
              contents: [{{
                parts: [
                  {{ text: "Analyse cette boîte de Monopoly. Identifie précisément le titre exact, l\\'année approximative, l\\'éditeur (Hasbro, Parker, Winning Moves, etc.), la catégorie (Classique, Villes & Régions, Pop Culture, Variantes, etc.) et les mots-clés distinctifs. Réponds UNIQUEMENT sous forme de JSON strict: {\\"title\\": \\"...\\", \\"year\\": \\"...\\", \\"publisher\\": \\"...\\", \\"category\\": \\"...\\", \\"barcode\\": \\"...\\"}" }},
                  {{ inline_data: {{ mime_type: mimeType, data: base64Data }} }}
                ]
              }}]
            }})
          }});
          const data = await response.json();
          if (data && data.candidates && data.candidates[0] && data.candidates[0].content) {{
            const rawText = data.candidates[0].content.parts[0].text;
            const jsonMatch = rawText.match(/\\{{[\\s\\S]*?\\}}/);
            if (jsonMatch) {{
              aiDetection = JSON.parse(jsonMatch[0]);
            }}
          }}
        }} catch(err) {{
          console.warn("Gemini vision analysis failed:", err);
        }}
      }}

      // 3. Fallback extraction from filename
      let queryGuess = "";
      if (aiDetection && aiDetection.title) {{
        queryGuess = aiDetection.title;
        detectedInfoFromScan = aiDetection;
      }} else if (detectedBarcode) {{
        queryGuess = detectedBarcode;
        detectedInfoFromScan = {{ barcode: detectedBarcode }};
      }} else if (fileName) {{
        let cleanName = fileName.replace(/\\.[^/.]+$/, "").replace(/[-_]/g, " ");
        cleanName = cleanName.replace(/box|boite|monopoly|recto|verso|front|back|img|photo/gi, "").trim();
        if (cleanName.length > 2) {{
          queryGuess = cleanName;
        }}
      }}

      overlay.style.display = "none";
      if (queryGuess) {{
        document.getElementById("scannerSearchQuery").value = queryGuess;
      }}
      searchAndRenderScannerCandidates(queryGuess || document.getElementById("scannerSearchQuery").value);
    }}

    function searchAndRenderScannerCandidates(query) {{
      const q = (query || "").trim().toLowerCase();
      let candidates = [];

      if (q) {{
        const tokens = q.split(/\\s+/).filter(function(t) {{ return t.length > 1; }});
        candidates = database.map(function(item) {{
          let score = 0;
          const nameLower = (item.name || "").toLowerCase();
          const descLower = (item.description || "").toLowerCase();
          const pubLower = (item.publisher || "").toLowerCase();
          const catLower = (item.category || "").toLowerCase();
          const yearStr = item.year ? item.year.toString() : "";
          const barStr = item.barcode ? item.barcode.toString().toLowerCase() : "";

          if (barStr && (barStr === q || q.includes(barStr))) score += 100;
          if (nameLower === q) score += 50;
          if (nameLower.includes(q)) score += 30;

          tokens.forEach(function(tok) {{
            if (nameLower.includes(tok)) score += 12;
            if (descLower.includes(tok)) score += 4;
            if (pubLower.includes(tok)) score += 3;
            if (catLower.includes(tok)) score += 3;
            if (yearStr === tok) score += 8;
          }});

          return {{ item: item, score: score }};
        }})
        .filter(function(res) {{ return res.score > 0; }})
        .sort(function(a, b) {{ return b.score - a.score; }})
        .slice(0, 8)
        .map(function(res) {{ return res.item; }});
      }} else {{
        candidates = database.slice(0, 5);
      }}

      renderScannerResults(candidates, q);
    }}

    function renderScannerResults(candidates, query) {{
      const container = document.getElementById("scannerResultArea");
      const statsLabel = document.getElementById("matchStatsLabel");

      if (candidates.length === 0) {{
        statsLabel.textContent = "Aucune correspondance directe trouvée";
        const prefillName = query ? ("Monopoly " + query.charAt(0).toUpperCase() + query.slice(1)) : "Monopoly (Nouvelle Édition)";
        const prefillYear = (detectedInfoFromScan && detectedInfoFromScan.year) ? detectedInfoFromScan.year : new Date().getFullYear();
        const prefillPub = (detectedInfoFromScan && detectedInfoFromScan.publisher) ? detectedInfoFromScan.publisher : "Hasbro";
        const prefillCat = (detectedInfoFromScan && detectedInfoFromScan.category) ? detectedInfoFromScan.category : "Thématique";

        container.innerHTML = 
          '<div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 16px; margin-bottom: 16px;">' +
            '<div style="display: flex; gap: 10px; align-items: flex-start;">' +
              '<span style="font-size: 1.5rem;">✨</span>' +
              '<div>' +
                '<h4 style="margin: 0 0 4px 0; color: #f59e0b; font-size: 1rem; font-weight: 700;">Édition non répertoriée dans le catalogue</h4>' +
                '<p style="margin: 0; font-size: 0.85rem; color: var(--text-muted);">' +
                  'Cette boîte ne semble pas encore faire partie des ' + database.length + ' références enregistrées. ' +
                  'Vous pouvez l\\'ajouter immédiatement au catalogue et définir son statut :' +
                '</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
          '<div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 18px;">' +
            '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 12px;">' +
              '<div>' +
                '<label style="display:block; font-size:0.75rem; font-weight:700; color:var(--text-muted); margin-bottom:4px;">Nom de l\\'édition *</label>' +
                '<input type="text" id="scanNewName" class="form-control" value="' + prefillName.replace(/"/g, '&quot;') + '" style="font-weight:600;">' +
              '</div>' +
              '<div>' +
                '<label style="display:block; font-size:0.75rem; font-weight:700; color:var(--text-muted); margin-bottom:4px;">Année de parution</label>' +
                '<input type="number" id="scanNewYear" class="form-control" value="' + prefillYear + '">' +
              '</div>' +
            '</div>' +
            '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 12px;">' +
              '<div>' +
                '<label style="display:block; font-size:0.75rem; font-weight:700; color:var(--text-muted); margin-bottom:4px;">Éditeur</label>' +
                '<input type="text" id="scanNewPublisher" class="form-control" value="' + prefillPub.replace(/"/g, '&quot;') + '">' +
              '</div>' +
              '<div>' +
                '<label style="display:block; font-size:0.75rem; font-weight:700; color:var(--text-muted); margin-bottom:4px;">Catégorie</label>' +
                '<input type="text" id="scanNewCategory" class="form-control" value="' + prefillCat.replace(/"/g, '&quot;') + '">' +
              '</div>' +
            '</div>' +
            '<div style="margin-bottom: 16px;">' +
              '<label style="display:block; font-size:0.75rem; font-weight:700; color:var(--text-muted); margin-bottom:4px;">Particularités / Description</label>' +
              '<input type="text" id="scanNewDesc" class="form-control" placeholder="Pions exclusifs, format de boîte, règles spécifiques...">' +
            '</div>' +
            '<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: flex-end; padding-top: 10px; border-top: 1px solid var(--border-color);">' +
              '<button class="btn btn-secondary" onclick="saveScannedNewEdition(\\'none\\')">⚪ Ajouter au catalogue seul</button>' +
              '<button class="btn btn-secondary" onclick="saveScannedNewEdition(\\'wishlist\\')" style="border-color: #f59e0b; color: #f59e0b;">⭐ Ajouter en Wishlist</button>' +
              '<button class="btn btn-primary" onclick="saveScannedNewEdition(\\'owned\\')" style="background: #10b981; border-color: #10b981;">🟢 Ajouter à ma Collection</button>' +
            '</div>' +
          '</div>';
        return;
      }}

      statsLabel.textContent = candidates.length + " correspondance(s) trouvée(s)";
      const topMatch = candidates[0];
      const isOwned = topMatch.status === "owned";
      const isWishlist = topMatch.status === "wishlist";

      let statusBadge = '<span class="status-badge none">⚪ Non possédé</span>';
      if (isOwned) statusBadge = '<span class="status-badge owned">🟢 Déjà dans votre Collection</span>';
      else if (isWishlist) statusBadge = '<span class="status-badge wishlist">⭐ Dans votre Wishlist</span>';

      let topMatchHtml = 
        '<div style="background: var(--bg-surface); border: 2px solid ' + (isOwned ? '#10b981' : 'var(--accent)') + '; border-radius: 10px; padding: 16px; margin-bottom: 16px;">' +
          '<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">' +
            '<div style="display: flex; align-items: center; gap: 8px;">' +
              '<span style="background: var(--accent); color: #fff; font-size: 0.72rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">Meilleure Correspondance</span>' +
              statusBadge +
            '</div>' +
            '<span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">Réf #' + topMatch.id + '</span>' +
          '</div>' +
          '<div style="display: flex; gap: 16px; align-items: center; flex-wrap: wrap;">' +
            (currentScannedDataUrl ? 
              '<div style="display: flex; gap: 8px; align-items: center; background: rgba(0,0,0,0.25); padding: 8px; border-radius: 8px;">' +
                '<div style="text-align: center;">' +
                  '<div style="font-size: 0.68rem; color: var(--text-muted); margin-bottom: 2px;">Votre Photo</div>' +
                  '<img src="' + currentScannedDataUrl + '" style="width: 70px; height: 70px; object-fit: contain; border-radius: 4px; border: 1px solid var(--border-color);">' +
                '</div>' +
                '<div style="font-size: 1.2rem; opacity: 0.4;">➔</div>' +
                '<div style="text-align: center;">' +
                  '<div style="font-size: 0.68rem; color: var(--text-muted); margin-bottom: 2px;">Jaquette Catalogue</div>' +
                  (topMatch.image_url ? 
                    '<img src="' + topMatch.image_url + '" style="width: 70px; height: 70px; object-fit: contain; border-radius: 4px; border: 1px solid var(--border-color);" onerror="handleImageError(this)">' :
                    '<div style="width: 70px; height: 70px; display: flex; align-items: center; justify-content: center; background: var(--bg-card); border-radius: 4px; font-weight: 800; color: var(--primary);">M</div>') +
                '</div>' +
              '</div>' : 
              (topMatch.image_url ? '<img src="' + topMatch.image_url + '" style="width: 70px; height: 70px; object-fit: contain; border-radius: 4px; border: 1px solid var(--border-color);">' : '')
            ) +
            '<div style="flex: 1; min-width: 220px;">' +
              '<h3 style="font-size: 1.15rem; font-weight: 800; color: var(--text-main); margin-bottom: 4px;">' + topMatch.name + '</h3>' +
              '<div style="display: flex; gap: 10px; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 6px; flex-wrap: wrap;">' +
                '<span>📅 ' + (topMatch.year || 'N/C') + '</span>' +
                '<span>🏢 ' + (topMatch.publisher || 'Hasbro') + '</span>' +
                '<span>📂 ' + (topMatch.category || 'Général') + '</span>' +
                '<span>📍 ' + (topMatch.country || 'International') + '</span>' +
              '</div>' +
              '<p style="font-size: 0.82rem; color: var(--text-muted); margin: 0; line-height: 1.4;">' + (topMatch.description || 'Édition officielle répertoriée.') + '</p>' +
            '</div>' +
          '</div>' +
          '<div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border-color); align-items: center; justify-content: flex-end;">' +
            (isOwned ? 
              '<span style="font-size: 0.82rem; color: #10b981; font-weight: 600; margin-right: auto;">✅ Cet article est déjà enregistré dans votre collection !</span>' +
              '<button class="btn btn-secondary" onclick="executeScannedAcquisition(\\'' + topMatch.id + '\\', \\'owned\\', true)" style="font-size: 0.8rem;">📸 Mettre à jour avec cette photo</button>' :
              '<button class="btn btn-secondary" onclick="executeScannedAcquisition(\\'' + topMatch.id + '\\', \\'wishlist\\')" style="border-color: #f59e0b; color: #f59e0b; font-size: 0.85rem;">⭐ Ajouter en Wishlist</button>' +
              '<button class="btn btn-primary" onclick="executeScannedAcquisition(\\'' + topMatch.id + '\\', \\'owned\\')" style="background: #10b981; border-color: #10b981; font-size: 0.85rem; font-weight: 700;">🟢 Je l\\'ai achetée (Ajouter à ma collection)</button>'
            ) +
          '</div>' +
        '</div>';

      let othersHtml = "";
      if (candidates.length > 1) {{
        othersHtml = '<div style="margin-top: 14px;"><div style="font-size: 0.78rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 8px;">Autres éditions similaires dans le catalogue :</div>';
        for (let i = 1; i < candidates.length; i++) {{
          const item = candidates[i];
          const itemOwned = item.status === "owned";
          othersHtml += 
            '<div class="candidate-card" onclick="selectScannerCandidate(\\'' + item.id + '\\')">' +
              (item.image_url ? 
                '<img src="' + item.image_url + '" style="width: 44px; height: 44px; object-fit: contain; border-radius: 4px; border: 1px solid var(--border-color);" onerror="handleImageError(this)">' :
                '<div style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; background: var(--bg-card); border-radius: 4px; font-weight: 800; color: var(--primary);">M</div>'
              ) +
              '<div style="flex: 1; min-width: 0;">' +
                '<div style="display: flex; justify-content: space-between; align-items: center;">' +
                  '<strong style="font-size: 0.9rem; color: var(--text-main); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">' + item.name + '</strong>' +
                  '<span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 8px;">' + (item.year || '') + '</span>' +
                '</div>' +
                '<div style="font-size: 0.75rem; color: var(--text-muted); display: flex; gap: 8px;">' +
                  '<span>' + (item.publisher || 'Hasbro') + '</span>' +
                  '<span>•</span>' +
                  '<span>' + (item.category || 'Général') + '</span>' +
                  (itemOwned ? '<span style="color: #10b981; font-weight: 700; margin-left: auto;">(Possédé)</span>' : '') +
                '</div>' +
              '</div>' +
              '<button class="btn btn-secondary" style="padding: 4px 10px; font-size: 0.75rem;" onclick="event.stopPropagation(); executeScannedAcquisition(\\'' + item.id + '\\', \\'owned\\');">🟢 Choisir</button>' +
            '</div>';
        }}
        othersHtml += '</div>';
      }}

      const notInCatalogHtml = 
        '<div style="text-align: center; margin-top: 16px; padding-top: 12px; border-top: 1px dashed var(--border-color);">' +
          '<button class="btn btn-secondary" onclick="renderScannerResults([], \\'' + (query || '').replace(/'/g, "\\\\'") + '\\')" style="font-size: 0.8rem;">' +
            '➕ Aucune de ces éditions ne correspond ? Créer une nouvelle référence' +
          '</button>' +
        '</div>';

      container.innerHTML = topMatchHtml + othersHtml + notInCatalogHtml;
    }}

    function selectScannerCandidate(id) {{
      const item = database.find(function(e) {{ return e.id === id; }});
      if (item) {{
        const filtered = database.filter(function(e) {{ return e.id !== id; }});
        renderScannerResults([item].concat(filtered.slice(0, 5)), "");
      }}
    }}

    function executeScannedAcquisition(id, targetStatus, updatePhotoOnly) {{
      const item = database.find(function(e) {{ return e.id === id; }});
      if (!item) return;

      if (!updatePhotoOnly) {{
        item.status = targetStatus;
        if (targetStatus === "owned" && !item.condition) {{
          item.condition = "Très bon état";
        }}
      }}

      if (currentScannedDataUrl) {{
        item.user_image = currentScannedDataUrl;
        if (!item.image_url) {{
          item.image_url = currentScannedDataUrl;
        }}
      }}

      saveDatabase();
      renderStats();
      renderList(false);
      closeScannerModal();

      const label = targetStatus === "owned" ? "🟢 Ajouté à votre collection !" : "⭐ Ajouté à votre liste de recherches !";
      showToast(item.name + " : " + (updatePhotoOnly ? "Photo mise à jour !" : label));
    }}

    function saveScannedNewEdition(targetStatus) {{
      const name = (document.getElementById("scanNewName").value || "").trim();
      if (!name) {{
        alert("Veuillez renseigner un titre pour cette édition.");
        return;
      }}
      const year = parseInt(document.getElementById("scanNewYear").value) || new Date().getFullYear();
      const pub = (document.getElementById("scanNewPublisher").value || "Hasbro").trim();
      const cat = (document.getElementById("scanNewCategory").value || "Général").trim();
      const desc = (document.getElementById("scanNewDesc").value || "").trim();

      const newId = "mono-custom-" + Date.now();
      const newItem = {{
        id: newId,
        name: name,
        year: year,
        publisher: pub,
        category: cat,
        country: "France",
        description: desc || "Édition ajoutée via le Scanner intelligent.",
        image_url: currentScannedDataUrl || "",
        user_image: currentScannedDataUrl || "",
        status: targetStatus,
        condition: targetStatus === "owned" ? "Très bon état" : "",
        price: "",
        value: "",
        location: targetStatus === "owned" ? "Collection personnelle" : "",
        notes: "Ajouté via Scanner le " + new Date().toLocaleDateString("fr-FR")
      }};

      database.unshift(newItem);
      saveDatabase();
      populateFilters();
      renderStats();
      renderList(true);
      closeScannerModal();

      const msg = targetStatus === "owned" 
        ? "🟢 " + name + " créé et ajouté à votre collection !" 
        : targetStatus === "wishlist"
        ? "⭐ " + name + " créé et mis en Wishlist !"
        : "⚪ " + name + " ajouté au catalogue des références !";
      showToast(msg);
    }}

    // INITIALIZATION & LISTENERS
    document.addEventListener("DOMContentLoaded", function() {{
      initDatabase();
      renderStats();
      populateFilters();
      renderList(true);

      document.getElementById("themeBtn").addEventListener("click", function() {{
        const body = document.body;
        const newTheme = body.getAttribute("data-theme") === "light" ? "dark" : "light";
        body.setAttribute("data-theme", newTheme);
      }});

      document.getElementById("searchInput").addEventListener("input", function(e) {{
        currentSearchTerm = e.target.value.trim();
        renderList(true);
      }});

      document.getElementById("countrySelect").addEventListener("change", function(e) {{
        currentCountry = e.target.value;
        renderList(true);
      }});

      document.getElementById("publisherSelect").addEventListener("change", function(e) {{
        currentPublisher = e.target.value;
        renderList(true);
      }});

      document.getElementById("decadeSelect").addEventListener("change", function(e) {{
        currentDecade = e.target.value;
        renderList(true);
      }});

      document.getElementById("sortSelect").addEventListener("change", function(e) {{
        currentSort = e.target.value;
        renderList(true);
      }});

      document.getElementById("loadMoreBtn").addEventListener("click", function() {{
        displayedCount += PAGE_SIZE;
        renderList(false);
      }});

      document.getElementById("cardViewBtn").addEventListener("click", function() {{
        currentView = "card";
        document.getElementById("cardViewBtn").classList.add("active");
        document.getElementById("tableViewBtn").classList.remove("active");
        renderList(false);
      }});

      document.getElementById("tableViewBtn").addEventListener("click", function() {{
        currentView = "table";
        document.getElementById("tableViewBtn").classList.add("active");
        document.getElementById("cardViewBtn").classList.remove("active");
        renderList(false);
      }});

      document.getElementById("statusPills").addEventListener("click", function(e) {{
        const pill = e.target.closest(".pill");
        if (!pill) return;
        document.querySelectorAll("#statusPills .pill").forEach(function(p) {{ p.classList.remove("active"); }});
        pill.classList.add("active");
        currentFilterStatus = pill.dataset.status;
        renderList(true);
      }});

      document.getElementById("categoryPills").addEventListener("click", function(e) {{
        const pill = e.target.closest(".pill");
        if (!pill) return;
        document.querySelectorAll("#categoryPills .pill").forEach(function(p) {{ p.classList.remove("active"); }});
        pill.classList.add("active");
        currentFilterCategory = pill.dataset.category;
        renderList(true);
      }});

      // Global delegation for clicks
      document.addEventListener("click", function(e) {{
        const cycleBtn = e.target.closest("[data-action='cycle']");
        if (cycleBtn && cycleBtn.dataset.id) {{
          cycleStatus(cycleBtn.dataset.id);
          return;
        }}

        const editBtn = e.target.closest(".edit-btn");
        if (editBtn && editBtn.dataset.id) {{
          openEditModal(editBtn.dataset.id);
          return;
        }}

        const boxWrapper = e.target.closest(".box-cover-wrapper, [data-lightbox-id]");
        if (boxWrapper && boxWrapper.dataset.lightboxId && !e.target.closest(".status-ribbon")) {{
          openLightbox(boxWrapper.dataset.lightboxId);
          return;
        }}
      }});

      // Lightbox Actions
      document.getElementById("closeLightbox").addEventListener("click", function() {{
        document.getElementById("lightboxModalBackdrop").classList.remove("open");
      }});
      document.getElementById("lightboxEditBtn").addEventListener("click", function() {{
        document.getElementById("lightboxModalBackdrop").classList.remove("open");
        if (activeLightboxId) openEditModal(activeLightboxId);
      }});

      // Edit Modal Actions
      document.getElementById("closeEditModal").addEventListener("click", function() {{
        document.getElementById("editModalBackdrop").classList.remove("open");
      }});
      document.getElementById("cancelEditBtn").addEventListener("click", function() {{
        document.getElementById("editModalBackdrop").classList.remove("open");
      }});
      document.getElementById("saveEditBtn").addEventListener("click", saveEditModal);

      document.getElementById("editImageUrl").addEventListener("input", function() {{
        const id = document.getElementById("editItemId").value;
        const item = database.find(function(e) {{ return e.id === id; }});
        updateEditPreview(item);
      }});

      document.getElementById("editImageFileInput").addEventListener("change", function(e) {{
        handleImageUpload(e.target.files[0], "editImageUrl", "modalImagePreviewContainer");
      }});

      document.getElementById("clearImageBtn").addEventListener("click", function() {{
        document.getElementById("editImageUrl").value = "";
        const id = document.getElementById("editItemId").value;
        const item = database.find(function(e) {{ return e.id === id; }});
        updateEditPreview(item);
      }});

      // Add Modal Actions
      document.getElementById("addCustomBtn").addEventListener("click", openAddModal);
      document.getElementById("closeAddModal").addEventListener("click", function() {{
        document.getElementById("addModalBackdrop").classList.remove("open");
      }});
      document.getElementById("cancelAddBtn").addEventListener("click", function() {{
        document.getElementById("addModalBackdrop").classList.remove("open");
      }});
      document.getElementById("confirmAddBtn").addEventListener("click", saveCustomEdition);

      document.getElementById("addImageUrl").addEventListener("input", function(e) {{
        const url = e.target.value.trim();
        const preview = document.getElementById("addModalImagePreview");
        if (url) {{
          preview.innerHTML = '<img src="' + url + '" style="width:100%; height:100%; object-fit:contain; border-radius:4px;">';
        }} else {{
          preview.innerHTML = '<span style="font-size:1.8rem; opacity:0.6;">📷</span>';
        }}
      }});

      document.getElementById("addImageFileInput").addEventListener("change", function(e) {{
        handleImageUpload(e.target.files[0], "addImageUrl", "addModalImagePreview");
      }});

      // Export / Import
      document.getElementById("exportCsvBtn").addEventListener("click", exportToCsv);
      document.getElementById("backupJsonBtn").addEventListener("click", backupToJson);
      document.getElementById("importJsonInput").addEventListener("change", importFromJson);

      // Box Scanner Events
      document.getElementById("scanBoxBtn").addEventListener("click", openScannerModal);
      document.getElementById("closeScannerModal").addEventListener("click", closeScannerModal);
      document.getElementById("closeScannerFooterBtn").addEventListener("click", closeScannerModal);

      const scannerDropzone = document.getElementById("scannerDropzone");
      const scannerFileInput = document.getElementById("scannerFileInput");

      document.getElementById("scannerPickFileBtn").addEventListener("click", function(e) {{
        e.stopPropagation();
        scannerFileInput.click();
      }});

      document.getElementById("scannerChangePhotoBtn").addEventListener("click", function(e) {{
        e.stopPropagation();
        scannerFileInput.click();
      }});

      scannerDropzone.addEventListener("click", function(e) {{
        if (e.target.closest("button") || e.target.closest("input")) return;
        scannerFileInput.click();
      }});

      scannerDropzone.addEventListener("dragover", function(e) {{
        e.preventDefault();
        scannerDropzone.style.borderColor = "var(--primary)";
        scannerDropzone.style.background = "rgba(225, 29, 72, 0.08)";
      }});

      scannerDropzone.addEventListener("dragleave", function(e) {{
        e.preventDefault();
        scannerDropzone.style.borderColor = "var(--accent)";
        scannerDropzone.style.background = "rgba(56, 189, 248, 0.03)";
      }});

      scannerDropzone.addEventListener("drop", function(e) {{
        e.preventDefault();
        scannerDropzone.style.borderColor = "var(--accent)";
        scannerDropzone.style.background = "rgba(56, 189, 248, 0.03)";
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {{
          handleScannerFile(e.dataTransfer.files[0]);
        }}
      }});

      scannerFileInput.addEventListener("change", function(e) {{
        if (e.target.files && e.target.files.length > 0) {{
          handleScannerFile(e.target.files[0]);
        }}
      }});

      document.getElementById("scannerSearchQuery").addEventListener("input", function(e) {{
        searchAndRenderScannerCandidates(e.target.value);
      }});

      document.getElementById("toggleAiKeyBtn").addEventListener("click", function() {{
        const row = document.getElementById("aiKeyConfigRow");
        row.style.display = row.style.display === "none" ? "block" : "none";
      }});

      document.getElementById("saveGeminiApiKeyBtn").addEventListener("click", function() {{
        const val = (document.getElementById("geminiApiKeyInput").value || "").trim();
        if (val) {{
          localStorage.setItem("gemini_api_key", val);
          showToast("Clé API Gemini enregistrée !");
        }} else {{
          localStorage.removeItem("gemini_api_key");
          showToast("Clé API Gemini supprimée.");
        }}
        updateAiBadgeStatus();
        document.getElementById("aiKeyConfigRow").style.display = "none";
      }});
    }});
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated index.html with {len(seed_data)} editions! File size: {len(html_content)} bytes")
