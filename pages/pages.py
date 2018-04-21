from selenium.webdriver.common.by import By

from browser import Browser


class Login(Browser):
    locator_dictionary = {
        'input_password': (By.CSS_SELECTOR, '[id="password"]'),
        'primary_btn': (By.CSS_SELECTOR, '[class="primaryBtn"]'),
        'error_msg': (By.CSS_SELECTOR, '[class="error"]'),
    }

    def enter_password(self, password):
        if password == 'correct':
            self.input_password.send_keys('pe2irb9D')
        elif password == 'incorrect':
            self.input_password.send_keys('!@#$%^&*()1285')

    def submit_password(self):
        self.primary_btn.click()

    def login_to_service(self):
        self.open_page('https://qarecruitment.egnyte.com/fl/ZlhEpCQ89o')
        self.enter_password('correct')
        self.submit_password()


class TopBar(Browser):
    locator_dictionary = {
        'folder_link_top_bar': (By.CSS_SELECTOR, '[class="folderLink-topbar"]'),
        'sort_dropdown': (By.CSS_SELECTOR, '[class="dropdown-toggle"]'),
        'sort_menu': (By.CSS_SELECTOR, '[class="dropdown-menu"]'),
        'sort_name': (By.CSS_SELECTOR, '[data-sort="name"]'),
        'sort_size': (By.CSS_SELECTOR, '[data-sort="size"]'),
        'asc_order': (By.CSS_SELECTOR, '[data-order="ASC"]'),
        'desc_order': (By.CSS_SELECTOR, '[data-order="DESC"]'),
        'file_name': (By.CSS_SELECTOR, '[class="name"]'),
        'select_all_checkbox': (
            By.CSS_SELECTOR,
            '.select-all-items .inner-wrapper'
        ),
        'download_btn': (By.CSS_SELECTOR, 'button.is-type-selected'),
        'chrome_download_link': (
            By.CSS_SELECTOR,
            'href="https://qarecruitment.egnyte.com/publicFolderDownload'
        )
    }

    def open_sort_menu(self):
        self.sort_dropdown.click()
        self.sort_menu

    def choose_data_sort(self, data_sort):
        self.open_sort_menu()
        if data_sort == 'Size':
            self.sort_size.click()
        elif data_sort == 'Name':
            self.sort_name.click()

    def choose_data_order(self, data_order):
        self.open_sort_menu()
        if data_order == 'Ascending':
            self.asc_order.click()
        elif data_order == "Descending":
            self.desc_order.click()

    def sort_elements(self, data_order):
        list_elements = self.find_elements('file_name')
        element_attribute = [x.get_attribute('title') for x in list_elements]
        lower_case_attribute = [x.lower()for x in element_attribute]
        if data_order == "Ascending":
            assert sorted(lower_case_attribute) == lower_case_attribute
        elif data_order == "Descending":
            assert sorted(lower_case_attribute, reverse=False) == lower_case_attribute

    def confirm_download(self):
        self.open_page('chrome://downloads')
        self.chrome_download_link
