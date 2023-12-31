from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from app.application import Application


# Allure command:
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/amazon_sign_in.feature


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    context.driver = webdriver.Firefox(
        executable_path='/Users/svetlanalevinsohn/careerist/python-selenium-automation/geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\brown\CureskinProject\geckodriver')


# context.driver = webdriver.Safari()

#### HEADLESS MODE ####
# driver_path = ChromeDriverManager().install()
# service = Service(driver_path)
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# context.driver = webdriver.Chrome(
# chrome_options=options,
# service=service
# )

#### BROWSERSTACK ####
# desired_cap = {
#     'browser': 'Firefox',
#     'os_version': '11',
#     'os': 'Windows',
#     'name': test_name
# }
# bs_user = ''
# bs_key = ''
# url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
# context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        #     '{"status":"failed", "reason": "Step failed"}}'
        # )

        # Attach a screenshot to Allure report in case the step fails:
        # allure.attach(
        #     context.driver.get_screenshot_as_png(),
        #     name=f'{step.name}.png',
        #     attachment_type=AttachmentType.PNG
        # )


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()