def set_styles():
    """Sets style for main GUI"""
    return """
    QMainWindow { background-color: #1f1f1f; }
    QTabWidget::pane { 
        border: 0; 
        background-color: #1f1f1f;
    }
    QTabBar::tab {
        background: #2e2e2e;
        color: #ffffff;
        padding: 10px;
        min-width: 80px;
        min-height: 30px;
        font: bold 12pt "Arial";
    }
    QTabBar::tab:selected {
        background: #1f1f1f;
    }
    QTabBar::tab:hover {
        background: #3e3e3e;
    }
    QTableWidget { background-color: #333333; color: #ffffff; font: 12pt Arial; }
    QHeaderView::section { background-color: #2e2e2e; color: #ffffff; font: bold 12pt Arial; }
    QTableWidget::item { padding: 5px; }
    """
