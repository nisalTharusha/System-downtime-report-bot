from selenium import webdriver
from Support.process import WebAutomation

if __name__ == "__main__":
    app = WebAutomation()
    app.Wfm_login()
    app.NavigateTo_neoSuper()
    app.Create_directory()

