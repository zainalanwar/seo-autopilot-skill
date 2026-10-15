"""
HTML Report Generator for SEO-Autopilot

Generates professional, interactive HTML reports from SEO audit data.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class HTMLReportGenerator:
    """Generate HTML reports from SEO audit data"""
    
    def __init__(self):
        self.version = "1.0.0"
    
    def generate(self, audit_data: Dict[str, Any], output_file: str) -> str:
        """
        Generate HTML report from audit data
        
        Args:
            audit_data: Dictionary containing audit results
            output_file: Path to save HTML file
            
        Returns:
            Path to generated file
        """
        html = self._build_html(audit_data)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)
        
        return output_file
    
    def _build_html(self, data: Dict[str, Any]) -> str:
        """Build complete HTML document"""
        url = data.get('url', 'Unknown')
        issues = data.get('issues', [])
        pages = data.get('pages', [])
        
        # Calculate score
        high = len([i for i in issues if i.get('severity') == 'high'])
        medium = len([i for i in issues if i.get('severity') == 'medium'])
        low = len([i for i in issues if i.get('severity') == 'low'])
        score = max(0, 100 - (high * 20 + medium * 10 + low * 5))
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEO Audit Report - {url}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>{self._get_css()}</style>
</head>
<body>
<div style="padding:16px;background:#fff4d6;color:#432d00;text-align:center;font-weight:bold">DEMONSTRATION REPORT — simulated issues, no site crawl or verified SEO findings.</div>
    <div class="container">
        {self._build_header(url)}
        {self._build_summary(score, high, medium, low, len(issues))}
        {self._build_stats_cards(high, medium, low)}
        {self._build_issues(issues)}
        {self._build_pages_table(pages)}
        {self._build_recommendations(score, issues)}
        {self._build_footer()}
    </div>
    <script>{self._get_js()}</script>
</body>
</html>"""
    
    def _get_css(self) -> str:
        """Return CSS styles"""
        return """
        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --success: #10b981;
            --success-light: #d1fae5;
            --warning: #f59e0b;
            --warning-light: #fef3c7;
            --danger: #ef4444;
            --danger-light: #fee2e2;
            --gray-50: #f9fafb;
            --gray-100: #f3f4f6;
            --gray-200: #e5e7eb;
            --gray-300: #d1d5db;
            --gray-500: #6b7280;
            --gray-700: #374151;
            --gray-900: #111827;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--gray-50);
            color: var(--gray-900);
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        /* Header */
        .header {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            padding: 3rem 2rem;
            border-radius: 1rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .header p {
            opacity: 0.9;
        }
        
        /* Cards */
        .card {
            background: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        .card h2 {
            font-size: 1.25rem;
            margin-bottom: 1rem;
            color: var(--gray-900);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Summary Section */
        .summary {
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 2rem;
            align-items: center;
        }
        
        .score-circle {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }
        
        .score-circle .score-value {
            font-size: 2.5rem;
            line-height: 1;
        }
        
        .score-circle .score-label {
            font-size: 0.875rem;
            opacity: 0.9;
        }
        
        .score-good { background: linear-gradient(135deg, #10b981, #059669); }
        .score-warning { background: linear-gradient(135deg, #f59e0b, #d97706); }
        .score-danger { background: linear-gradient(135deg, #ef4444, #dc2626); }
        
        .score-info h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        
        .score-info p {
            color: var(--gray-500);
        }
        
        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .stat-card {
            background: white;
            border-radius: 0.75rem;
            padding: 1.25rem;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            border-top: 4px solid;
        }
        
        .stat-card.total { border-color: var(--primary); }
        .stat-card.high { border-color: var(--danger); }
        .stat-card.medium { border-color: var(--warning); }
        .stat-card.low { border-color: var(--success); }
        
        .stat-card .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--gray-900);
        }
        
        .stat-card .stat-label {
            font-size: 0.875rem;
            color: var(--gray-500);
            margin-top: 0.25rem;
        }
        
        /* Badges */
        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .badge-high { background: var(--danger-light); color: var(--danger); }
        .badge-medium { background: var(--warning-light); color: #d97706; }
        .badge-low { background: var(--success-light); color: #059669; }
        
        /* Issues */
        .issues-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .filters {
            display: flex;
            gap: 0.5rem;
        }
        
        .filter-btn {
            padding: 0.5rem 1rem;
            border: 1px solid var(--gray-200);
            background: white;
            border-radius: 0.375rem;
            cursor: pointer;
            font-size: 0.875rem;
            transition: all 0.2s;
        }
        
        .filter-btn:hover {
            background: var(--gray-100);
        }
        
        .filter-btn.active {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }
        
        .issue-card {
            border: 1px solid var(--gray-200);
            border-left: 4px solid;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            overflow: hidden;
            transition: all 0.2s;
        }
        
        .issue-card:hover {
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        .issue-card.severity-high { border-left-color: var(--danger); }
        .issue-card.severity-medium { border-left-color: var(--warning); }
        .issue-card.severity-low { border-left-color: var(--success); }
        
        .issue-header {
            padding: 1rem 1.25rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            background: white;
        }
        
        .issue-header:hover {
            background: var(--gray-50);
        }
        
        .issue-title {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .issue-title h4 {
            font-size: 1rem;
            font-weight: 600;
        }
        
        .issue-title .url {
            font-size: 0.875rem;
            color: var(--gray-500);
        }
        
        .issue-toggle {
            font-size: 1.25rem;
            color: var(--gray-500);
            transition: transform 0.2s;
        }
        
        .issue-card.expanded .issue-toggle {
            transform: rotate(180deg);
        }
        
        .issue-body {
            display: none;
            padding: 0 1.25rem 1.25rem;
            background: var(--gray-50);
            border-top: 1px solid var(--gray-200);
        }
        
        .issue-card.expanded .issue-body {
            display: block;
        }
        
        .fix-box {
            background: white;
            border: 1px solid #bae6fd;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-top: 1rem;
        }
        
        .fix-box h5 {
            color: var(--primary);
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .fix-box p {
            margin-bottom: 0.75rem;
            color: var(--gray-700);
        }
        
        .copy-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            cursor: pointer;
            font-size: 0.875rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: background 0.2s;
        }
        
        .copy-btn:hover {
            background: var(--primary-dark);
        }
        
        .copy-btn.copied {
            background: var(--success);
        }
        
        /* Pages Table */
        .pages-table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .pages-table th,
        .pages-table td {
            padding: 0.875rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--gray-200);
        }
        
        .pages-table th {
            background: var(--gray-50);
            font-weight: 600;
            font-size: 0.875rem;
            text-transform: uppercase;
            color: var(--gray-500);
        }
        
        .pages-table tr:hover {
            background: var(--gray-50);
        }
        
        .status-icon {
            font-size: 1.25rem;
        }
        
        .status-ok { color: var(--success); }
        .status-warn { color: var(--warning); }
        .status-error { color: var(--danger); }
        
        /* Recommendations */
        .recommendation {
            background: linear-gradient(135deg, #eff6ff, #dbeafe);
            border-radius: 0.5rem;
            padding: 1.25rem;
            margin-bottom: 1rem;
        }
        
        .recommendation h3 {
            color: var(--primary);
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .recommendation ol {
            padding-left: 1.25rem;
        }
        
        .recommendation li {
            margin-bottom: 0.5rem;
        }
        
        /* Footer */
        footer {
            text-align: center;
            padding: 2rem;
            color: var(--gray-500);
            font-size: 0.875rem;
        }
        
        footer a {
            color: var(--primary);
            text-decoration: none;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .summary {
                grid-template-columns: 1fr;
                text-align: center;
            }
            
            .score-circle {
                margin: 0 auto;
            }
        }
        
        @media print {
            .no-print { display: none !important; }
            .card { break-inside: avoid; }
            body { background: white; }
        }
        """
    
    def _get_js(self) -> str:
        """Return JavaScript for interactivity"""
        return """
        // Toggle issue details
        function toggleIssue(element) {
            const card = element.closest('.issue-card');
            card.classList.toggle('expanded');
        }
        
        // Copy to clipboard
        async function copyToClipboard(text, button) {
            try {
                await navigator.clipboard.writeText(text);
                button.innerHTML = '✓ Copied!';
                button.classList.add('copied');
                setTimeout(() => {
                    button.innerHTML = '📋 Copy';
                    button.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy:', err);
            }
        }
        
        // Filter issues
        function filterIssues(severity) {
            // Update active button
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Filter cards
            document.querySelectorAll('.issue-card').forEach(card => {
                if (severity === 'all') {
                    card.style.display = 'block';
                } else {
                    const cardSeverity = card.classList.contains('severity-' + severity);
                    card.style.display = cardSeverity ? 'block' : 'none';
                }
            });
        }
        
        // Print report
        function printReport() {
            window.print();
        }
        
        // Export as PDF (placeholder)
        function exportPDF() {
            alert('PDF export would be triggered here. Use Ctrl+P to print/save as PDF.');
        }
        """
    
    def _build_header(self, url: str) -> str:
        """Build report header"""
        return f"""
        <div class="header">
            <h1>🔍 SEO Audit Report</h1>
            <p><strong>URL:</strong> {url}</p>
            <p><strong>Generated:</strong> {datetime.now().strftime('%B %d, %Y at %H:%M')}</p>
            <div class="no-print" style="margin-top: 1rem;">
                <button onclick="printReport()" style="background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.3); padding: 0.5rem 1rem; border-radius: 0.375rem; cursor: pointer; margin-right: 0.5rem;">
                    🖨️ Print Report
                </button>
                <button onclick="exportPDF()" style="background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.3); padding: 0.5rem 1rem; border-radius: 0.375rem; cursor: pointer;">
                    📥 Export PDF
                </button>
            </div>
        </div>
        """
    
    def _build_summary(self, score: int, high: int, medium: int, low: int, total: int) -> str:
        """Build executive summary"""
        score_class = 'score-good' if score >= 80 else 'score-warning' if score >= 60 else 'score-danger'
        score_text = 'Excellent' if score >= 80 else 'Good' if score >= 60 else 'Needs Improvement'
        
        return f"""
        <div class="card">
            <h2>📊 Executive Summary</h2>
            <div class="summary">
                <div class="score-circle {score_class}">
                    <span class="score-value">{score}</span>
                    <span class="score-label">/ 100</span>
                </div>
                <div class="score-info">
                    <h3>SEO Score: {score_text}</h3>
                    <p>Your website has <strong>{total}</strong> issues that need attention. 
                    {'Focus on fixing high-priority issues first for maximum impact.' if high > 0 else 'Great job! Your SEO health looks good.'}</p>
                </div>
            </div>
        </div>
        """
    
    def _build_stats_cards(self, high: int, medium: int, low: int) -> str:
        """Build statistics cards"""
        total = high + medium + low
        return f"""
        <div class="stats-grid">
            <div class="stat-card total">
                <div class="stat-value">{total}</div>
                <div class="stat-label">Total Issues</div>
            </div>
            <div class="stat-card high">
                <div class="stat-value">{high}</div>
                <div class="stat-label">High Priority</div>
            </div>
            <div class="stat-card medium">
                <div class="stat-value">{medium}</div>
                <div class="stat-label">Medium Priority</div>
            </div>
            <div class="stat-card low">
                <div class="stat-value">{low}</div>
                <div class="stat-label">Low Priority</div>
            </div>
        </div>
        """
    
    def _build_issues(self, issues: List[Dict]) -> str:
        """Build detailed issues list"""
        if not issues:
            return """
            <div class="card">
                <h2>✅ No Demonstration Issues</h2>
                <p>No simulated issues were supplied. This does not mean the site has no SEO issues.</p>
            </div>
            """
        
        issues_html = ""
        for i, issue in enumerate(issues):
            severity = issue.get('severity', 'medium')
            fix = issue.get('fix', issue.get('suggestion', ''))
            
            issues_html += f"""
            <div class="issue-card severity-{severity}" id="issue-{i}">
                <div class="issue-header" onclick="toggleIssue(this)">
                    <div class="issue-title">
                        <span class="badge badge-{severity}">{severity}</span>
                        <div>
                            <h4>{issue.get('title', 'Unknown Issue')}</h4>
                            <span class="url">{issue.get('affected_url', 'N/A')}</span>
                        </div>
                    </div>
                    <span class="issue-toggle">▼</span>
                </div>
                <div class="issue-body">
                    <p><strong>Issue Type:</strong> {issue.get('type', 'N/A')}</p>
                    {f'''<div class="fix-box">
                        <h5>🤖 AI-Generated Fix</h5>
                        <p>{fix}</p>
                        <button class="copy-btn" onclick="event.stopPropagation(); copyToClipboard(`{fix}`, this)">
                            📋 Copy
                        </button>
                    </div>''' if fix else ''}
                </div>
            </div>
            """
        
        return f"""
        <div class="card">
            <div class="issues-header">
                <h2>🔧 Detailed Issues</h2>
                <div class="filters no-print">
                    <button class="filter-btn active" onclick="filterIssues('all')">All</button>
                    <button class="filter-btn" onclick="filterIssues('high')">High</button>
                    <button class="filter-btn" onclick="filterIssues('medium')">Medium</button>
                    <button class="filter-btn" onclick="filterIssues('low')">Low</button>
                </div>
            </div>
            {issues_html}
        </div>
        """
    
    def _build_pages_table(self, pages: List[Dict]) -> str:
        """Build pages analysis table"""
        if not pages:
            return """
            <div class="card">
                <h2>📄 Page Analysis</h2>
                <p>No page data available.</p>
            </div>
            """
        
        rows = ""
        for page in pages:
            issues_count = page.get('issues', 0)
            if issues_count == 0:
                status_class = 'status-ok'
                status_icon = '✅'
            elif issues_count < 3:
                status_class = 'status-warn'
                status_icon = '⚠️'
            else:
                status_class = 'status-error'
                status_icon = '❌'
            
            rows += f"""
            <tr>
                <td><strong>{page.get('url', 'N/A')}</strong></td>
                <td class="{status_class}">{status_icon}</td>
                <td>{issues_count}</td>
                <td>{page.get('score', 'N/A')}</td>
            </tr>
            """
        
        return f"""
        <div class="card">
            <h2>📄 Page Analysis</h2>
            <table class="pages-table">
                <thead>
                    <tr>
                        <th>Page URL</th>
                        <th>Status</th>
                        <th>Issues</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
        """
    
    def _build_recommendations(self, score: int, issues: List[Dict]) -> str:
        """Explain the limits of this demonstration instead of predicting impact."""
        return """<div class="card"><h2>Review before acting</h2>
        <p>The issues and score are simulated. Inspect the actual page HTML and
        collect measurements before deciding whether a change is needed.</p>
        <p>This report does not predict rankings, traffic gains or implementation time.</p></div>"""

    def _build_footer(self) -> str:
        """Build report footer"""
        return f"""
        <footer>
            <p>Generated by <strong>SEO-Autopilot Skill v{self.version}</strong></p>
            <p>Powered by <strong>MiMo v2.5-pro</strong> | 
            <a href="https://github.com/zainalanwar/seo-autopilot-skill" target="_blank">GitHub</a></p>
        </footer>
        """
