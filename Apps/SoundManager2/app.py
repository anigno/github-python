from flask import Flask, render_template, request, redirect, url_for

from Apps.SoundManager2.common.utils import get_hash_code

class SoundsManager:
    def __init__(self):
        self.logged_in = False
        self.correct_hash = "efbd1f26a54875e39972ccf7fa21a34f2491c850b2eba9636cb5478e595897b5"
        self.app = Flask('SoundsManager')
        self.app.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/button_click', 'button_click', self.button_click, methods=['POST'])
        self.app.add_url_rule('/set_scroll_value', 'set_scroll_value', self.set_scroll_value, methods=['POST'])
        self.app.add_url_rule('/get_scroll_value', 'get_scroll_value', self.get_scroll_value, methods=['GET'])
        self.app.add_url_rule('/update_status_text', 'update_status_text', self.update_status_text, methods=['POST'])
        self.app.add_url_rule('/get_status_text', 'get_status_text', self.get_status_text, methods=['GET'])

        self.scroll_value = 50  # Default scroll value
        self.status_text = "Initial Status"  # Default status text

    def login(self):
        if request.method == 'POST':
            password = request.form['password']
            password_hash = get_hash_code(password)
            if password_hash == self.correct_hash:
                self.logged_in = True
                return redirect(url_for('index'))
            else:
                return render_template('login.html', error="Invalid credentials")
        return render_template('login.html')

    def index(self):
        if not self.logged_in:
            return redirect(url_for('login'))
        return render_template('index.html', scroll_value=self.scroll_value, status_text=self.status_text)

    def button_click(self):
        self.update_status("B" + str(self.scroll_value))
        return ''

    def set_scroll_value(self):
        self.scroll_value = int(request.form.get('scroll_val'))
        self.update_status("S" + str(self.scroll_value))

        return ''

    def get_scroll_value(self):
        return str(self.scroll_value)

    def update_status_text(self):
        new_status_text = request.form.get('status_text')
        if new_status_text:
            self.update_status(new_status_text)
        return ''

    def get_status_text(self):
        return self.status_text

    def update_status(self, new_status_text):
        self.status_text = new_status_text

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    sounds_manager = SoundsManager()
    sounds_manager.run()
