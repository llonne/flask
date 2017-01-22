from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Show homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show application form."""

    job_list = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", jobs=job_list)


@app.route("/application-success", methods=["POST"])
def application_success():
    """Show application form."""

    fname = request.form.get("firstname")
    lname = request.form.get("lastname")
    salary = format_currency(float(request.form.get("salaryreq")))
    title = request.form.get("jobtitle")

    return render_template("application-response.html",
                           first_name=fname,
                           last_name=lname,
                           salary_req=salary,
                           job_title=title)


def format_currency(value):
    """Convert number to currency format."""
    return "${:,.2f}".format(value)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
