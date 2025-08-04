import json
import certifi

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest


class Interface(BoxLayout):

    def fetched(self, req_body, results):
        polarity = str(results[0])
        subjectivity = str(results[1])

        self.ids.lbl.text = f'Polarity: {polarity} \nSubjectivity: {subjectivity}'


    def failed(self, request, result):
        print(f'Request: {request} \nResult: {result}')


    def error(self, request, result):
        print(f'Error \nRequest: {request} \nResult: {result}')

        print(
            f'''
        URL: {request.url}
        Method: {request._method}
        required_body: {request.req_body}
        required_headers: {request.req_headers}
            ''')

        if hasattr(result, "code"):
            print(f'Status Code: {result.code}')
        else:
            print("No Status Code")


    def analyze(self):
        data = json.dumps({'sentence': self.ids.textInput.text})

        UrlRequest(
            url='https://kivy-text-analyzer-2qf4gjkww-alfreds-projects-2de87f9b.vercel.app/analyze/',
            method='POST',
            on_success=self.fetched,
            on_failure=self.failed,
            on_error=self.error,
            req_body=data,
            req_headers={'Content-Type': 'application/json; charset=utf-8'},
            ca_file=certifi.where(),
            verify=True
        )


class AnalyzerApp(App):
    pass


if __name__ == '__main__':
    AnalyzerApp().run()
