# ui_web.py
# Jonathan Wayne Abner — Web Dashboard for Harmonic Engine

from flask import Flask, render_template_string, request
import harmonic_engine_part3 as cosmic
import harmonic_engine_part4 as perpetual
import io, sys

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Harmonic Engine Dashboard</title>
<h1>Harmonic Engine Dashboard</h1>

<form method="post">
  <button name="action" value="quasar">Quasar Profile</button>
  <button name="action" value="horizon">Event Horizon</button>
  <button name="action" value="disk">Accretion Disk</button>
  <button name="action" value="perpetual">Perpetual Motion</button>
</form>

<pre>{{ output }}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    action = request.form.get("action")

    if action == "quasar":
        output = cosmic.quasar_profile()

    elif action == "horizon":
        output = cosmic.event_horizon_profile()

    elif action == "disk":
        output = cosmic.accretion_disk_profile()

    elif action == "perpetual":
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        perpetual.run_perpetual_engine()
        sys.stdout = old
        output = buf.getvalue()

    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    app.run(debug=True)
