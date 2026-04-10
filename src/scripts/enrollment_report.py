from yattag import Doc  # library to generate HTML easily
from dao.enrollment_dao import EnrollmentDAO  # DAO to fetch data


def generate_enrollment_report():
    # Create DAO instance to access database
    dao = EnrollmentDAO()

    # Fetch real enrollment data from DB
    rows = dao.get_all_enrollments_report()

    # Table headers (column names for HTML table)
    headers = ['First Name', 'Last Name', 'Email', 'Major', 'Course', 'Enrollment Date']

    doc, tag, text = Doc().tagtext()

    doc.asis('<!DOCTYPE html>')

    # Start HTML document
    with tag('html'):

        # HEAD section (metadata)
        with tag('head'):

            # Page title (shown in browser tab)
            with tag('title'):
                text("Enrollment Report")

        with tag('body'):
            with tag('h1'):
                text("All Students Enrolled")

            # Create table with some basic styling
            with tag('table', border='1', cellpadding='5', cellspacing='0'):

                # Create header row
                with tag('tr'):
                    for h in headers:
                        with tag('th'):  # table header cell
                            text(h)

                # Loop through each row from database
                for row in rows:

                    # Create a new table row
                    with tag('tr'):

                        # Loop through each column value in the row
                        for cell in row:

                            # Create table data cell
                            with tag('td'):
                                text(str(cell))  # convert value to string

    # Convert the built HTML document into a string
    result = doc.getvalue()

    # Write the HTML string into a file
    with open("report.html", "w") as f:
        f.write(result)

    # Print confirmation message in terminal
    print("Report generated: report.html")