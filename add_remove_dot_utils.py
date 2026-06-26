from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def append_dot(driver, desc_element):
    """Append a dot unconditionally to an <input> or <textarea> element and dispatch events."""
    current = desc_element.get_attribute("value") or ""
    new_value = current + "."
    driver.execute_script(
        """
        arguments[0].value = arguments[1];
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """,
        desc_element,
        new_value,
    )

def remove_trailing_dot(driver, desc_element):
    """Remove a single trailing dot from an <input> or <textarea> element (if present).
       Returns True if a change was made, False otherwise."""
    current = desc_element.get_attribute("value") or ""
    if current.endswith("."):
        new_value = current[:-1]
        driver.execute_script(
            """
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """,
            desc_element,
            new_value,
        )
        return True
    return False