from setuptools import setup


# def readme():
#     with open("README.rst") as file:
#         return file.read()


setup(name="pandoc-html-pdf-img",
      version=0.9,
      description=("Helps with processing of pdfs in Marked"),
      # long_description=readme(),
      author="Scott Hartley",
      author_email="scott.hartley@miamioh.edu",
      url="https://hartleygroup.org",
      license="MIT",
      scripts=["pandoc-html-pdf-img"],
      packages=["pandoc_html_pdf_img"],
      install_requires=["pandocfilters"],
      python_requires=">=3",
      )
