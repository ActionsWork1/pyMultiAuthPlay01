from playwright._impl._locator import Locator
from playwright._impl._page import Page


class TableHelpers:
    def __init__(self, page: Page, table_selector: str):
        self.page = page
        self.table: Locator = page.locator(table_selector)

    # ---------- Headers ----------
    def headers(self):
        """
        :description: headers of table
        :return:
        """
        return self.table.locator("thead th")

    def column_index(self, column_name: str):
        """
        :description: index of column in table
        :param column_name:
        :return:
        """
        headers = self.headers().all_inner_texts()
        return headers.index(column_name)

    # ---------- Rows ----------
    def rows(self):
        """
        :description: rows of table
        :return:
        """
        return self.table.locator("tbody tr")

    def rows_count(self):
        """
        :description: rows of table
        :return:
        """
        return self.table.locator("tbody tr").all()

    def row(self, text: str):
        """Return row containing given text"""
        return self.rows().filter(has_text=text).first

    # ---------- Cells ----------
    def cell(self, row_text: str, column_name: str):
        """
        :description: cell of given text
        :param row_text: text of row
        :param column_name: name of column
        :return: cell of given text in table
        """
        col_index = self.column_index(column_name)
        return self.row(row_text).locator("td").nth(col_index)

    # ---------- Actions ----------
    def click(self, row_text: str, column_name: str):
        self.cell(row_text, column_name).click()

    def text(self, row_text: str, column_name: str):
        return self.cell(row_text, column_name).inner_text()

    def contains(self, column_name: str, value: str):
        """
        :description: contains given value
        :param column_name:
        :param value:
        :return:
        """
        col_index = self.column_index(column_name)
        return self.rows().locator(f"td:nth-child({col_index + 1})").filter(has_text=value)




from playwright.sync_api import Page, Locator

class TableHelpers1:
    def __init__(self, page: Page, table_selector: str):
        self.page = page
        self.table: Locator = page.locator(table_selector)

    # ---------- Headers ----------
    def headers(self) -> Locator:
        return self.table.locator("thead th")

    def column_names(self) -> list[str]:
        """Returns a list of all column header texts."""
        return self.headers().all_inner_texts()

    def column_index(self, column_name: str) -> int:
        headers = self.column_names()
        try:
            # Note: Using .strip() helps if there are hidden spaces in HTML
            return [h.strip().upper() for h in headers].index(column_name.upper())
        except ValueError:
            raise ValueError(f"Column '{column_name}' not found. Available: {headers}")

    # ---------- Rows ----------
    def rows(self) -> Locator:
        return self.table.locator("tbody tr")

    def row_count(self) -> int:
        """Returns the number of rows currently displayed."""
        return self.rows().count()

    def row_by_text(self, text: str) -> Locator:
        """Finds the specific row containing unique text (like an email)."""
        return self.rows().filter(has_text=text).first

    # ---------- Cells & Data ----------
    def cell(self, row_text: str, column_name: str) -> Locator:
        col_index = self.column_index(column_name)
        return self.row_by_text(row_text).locator("td").nth(col_index)

    def get_row_data(self, row_index: int) -> dict:
        """Returns a dictionary of {ColumnName: Value} for a specific row index."""
        cols = self.column_names()
        # Filter out empty strings/headers like checkboxes or actions
        cells = self.rows().nth(row_index).locator("td").all_inner_texts()
        return dict(zip(cols, cells))

    # ---------- UI Interactions ----------
    def search(self, query: str):
        """Types into the 'Search records...' input field."""
        self.page.get_by_placeholder("Search records...").fill(query)
        self.page.locator("button[type='submit']>span:has-text('search')").click()
        self.page.wait_for_load_state("networkidle") # Wait for results to filter

    def toggle_switch(self, row_text: str, column_name: str):
        """
        Clicks the toggle switch in STATUS or BANNED columns.
        """
        cell = self.cell(row_text, column_name)
        # Locates the slider/input within the cell
        cell.locator("label span, input[type='checkbox']").first.click()

    def click_action(self, row_text: str, action: str):
        """
        Clicks 'edit' or 'delete' buttons in the ACTIONS column.
        :param action: 'edit' or 'delete'
        """
        row = self.row_by_text(row_text)
        if action.lower() == "edit":
            # row.locator("button:has(.fa-pencil), .btn-outline-primary").click()
            row.locator("div>a[title='Edit']").click()
        elif action.lower() == "delete":
            # row.locator("button:has(.fa-trash), .btn-outline-danger").click()
            row.locator("button[data-table='users']>span").click()

    # ---------- Assertions ----------
    def is_row_present(self, text: str) -> bool:
        return self.row_by_text(text).is_visible()