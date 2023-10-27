from playwright.sync_api import TimeoutError


class HtmlElement:
    def __init__(self, page, selector):
        self.page = page
        self.selector = selector

    def wait_for(self, seconds):
        self.page.wait_for_timeout(seconds * 1000)

    def find_element(self, timeout=30):
        self.page.wait_for_load_state('load')  # Чекаємо завантаження сторінки
        return self.page.locator(self.selector).wait_for(timeout=timeout * 1000)

    def is_element_visible(self, timeout=30):
        try:
            element = self.find_element(timeout)
            return element.is_visible()
        except TimeoutError:
            return False

    def is_element_present_in_the_dom(self, timeout=30):
        try:
            self.find_element(timeout)
            return True
        except TimeoutError:
            return False

    def get_attribute(self, attribute_name, timeout=30):
        try:
            element = self.find_element(timeout)
            return element.get_attribute(attribute_name)
        except TimeoutError:
            print(f"Can't find element with selector {self.selector} after {timeout} seconds.")

    def get_text(self, timeout=30):
        element = self.find_element(timeout)
        return element.text()

    def get_value_of_css_property(self, property_name, timeout=30):
        element = self.find_element(timeout)
        return element.evaluate(f'element => getComputedStyle(element).getPropertyValue("{property_name}")')

    def is_clickable(self, timeout=30):
        try:
            element = self.find_element(timeout)
            return element.is_enabled()
        except TimeoutError:
            return False

    def hover(self, timeout=30):
        element = self.find_element(timeout)
        element.hover()

    def scroll_into_view(self):
        try:
            element = self.find_element(timeout=5)
            element.scroll_into_view_if_needed()
        except TimeoutError:
            print(f"Can't find element with selector {self.selector} after 5 seconds.")
