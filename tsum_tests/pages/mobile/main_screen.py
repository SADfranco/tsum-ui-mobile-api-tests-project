from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class MainScreen:

    def skip_first_notifications(self):
        with step('Skip first notifications'):
            browser.element((AppiumBy.ID, "ru.tsum.app:id/gender_background_image")).click()
            browser.element((AppiumBy.ID, "ru.tsum.app:id/confirm_button")).click()
            browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")).click()

    def open_tab(self, main_tabs):
        with step(f'Opne tab "{main_tabs.tab_name}"'):
            browser.element((AppiumBy.ID, f"ru.tsum.app:id/{main_tabs.tab_name}_graph")).click()

    def check_bar_menu_title(self, main_tabs):
        with step(f'Check tab "{main_tabs.title_name}"'):
            browser.element((AppiumBy.ID, "ru.tsum.app:id/title_text")).should(
                have.exact_text(f'{main_tabs.title_name}'))


main_screen = MainScreen()
