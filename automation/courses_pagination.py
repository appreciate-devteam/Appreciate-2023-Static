template = """
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="Template Mo">
  <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900" rel="stylesheet">

  <title>Appreciate 2023</title>

  <!-- Bootstrap core CSS -->
  <link href="../../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link rel="shortcut icon" href="../../assets/images/tab.png" type="image/x-icon">

  <!-- Additional CSS Files -->
  <link rel="stylesheet" href="../../assets/css/fontawesome.css">
  <link rel="stylesheet" href="../../assets/css/templatemo-edu-meeting.css">
  <link rel="stylesheet" href="../../assets/css/owl.css">
  <link rel="stylesheet" href="../../assets/css/lightbox.css">
  <!--

-->
</head>

<body>



  <!-- Sub Header -->
  <div class="sub-header">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-sm-8">
          <div class="left-content">
            <p></p>
          </div>
        </div>
        <div class="col-lg-4 col-sm-4">
          <div class="right-icons">
            <ul>

            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ***** Header Area Start ***** -->
  <header class="header-area header-sticky">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <nav class="main-nav">
            <!-- ***** Logo Start ***** -->
            <a href="../../index.html" class="logo">
              2023 | APPRECIATE
            </a>
            <!-- ***** Logo End ***** -->
            <!-- ***** Menu Start ***** -->
            <ul class="nav">
              <li><a href="../../index.html">Home</a></li>
              <li><a href="" class="active">Studies</a></li>
            </ul>
            <a class='menu-trigger'>
              <span>Menu</span>
            </a>
            <!-- ***** Menu End ***** -->
          </nav>
        </div>
      </div>
    </div>
  </header>
  <!-- ***** Header Area End ***** -->

  <section class="heading-page header-text" id="top">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <h6>Here are our future Engineers</h6>
          <h2>ARE BORN</h2>
        </div>
      </div>
    </div>
  </section>

  <section class="meetings-page" id="meetings">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="row">
            <div class="col-lg-12">
              <div class="filters">
                <ul>
                  <li class="active">All Studies</li>
                  <li >ECE</li>
                  <li >EE</li>
                  <li >CE</li>
                  <li >ME</li>
                </ul>
              </div>
            </div>
            
            {div}

                

            
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <p>Copyright © 2023 Appreciate. All Rights Reserved. </p>
    </div>
  </section>


  <!-- Scripts -->
  <!-- Bootstrap core JavaScript -->
  <script src="../../vendor/jquery/jquery.min.js"></script>
  <script src="../../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <script src="../../assets/js/isotope.min.js"></script>
  <script src="../../assets/js/owl-carousel.js"></script>
  <script src="../../assets/js/lightbox.js"></script>
  <script src="../../assets/js/tabs.js"></script>
  <script src="../../assets/js/isotope.js"></script>
  <script src="../../assets/js/video.js"></script>
  <script src="../../assets/js/slick-slider.js"></script>
  <script src="../../assets/js/custom.js"></script>

</body>

</html>
"""


temp = """

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study}"><img src="../../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study}">
                        <h4>{title}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>
"""

div = ''
ece_codes = []
ece_titles = []
ece_abstracts = []

ee_codes = []
ee_titles = []
ee_abstracts = []

me_codes = []
me_titles = []
me_abstracts = []

ce_codes = []
ce_titles = []
ce_abstracts = []
import random
import csv
with open(r'studies.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    count = 0
    for row in reader:
        count += 1
        dept = row['dept']
        code = row['code']
        title = row['title'][:45]
        abstract = row['abstract_raw'][:60]

        if dept == 'CE':
            ce_codes.append(code)
            ce_titles.append(title)
            ce_abstracts.append(abstract)
        elif dept == 'ME':
            me_codes.append(code)
            me_titles.append(title)
            me_abstracts.append(abstract)
        elif dept == 'EE':
            ee_codes.append(code)
            ee_titles.append(title)
            ee_abstracts.append(abstract)
        elif dept == 'ECE':
            ece_codes.append(code)
            ece_titles.append(title)
            ece_abstracts.append(abstract)

print(len(ece_codes))
print(len(ee_codes))
print(len(ce_codes))
print(len(me_codes))
print(ece_codes)
pages = []
for index, study in enumerate(ee_codes):
    print(study)
    
    div += temp.format(title=ee_titles[index], abstract=ee_abstracts[index], study=f'../../abstracts/{study}.html') + f'\n\n'


filename = f'../paginated abstract list/ee/studies_ee.html'
with open(filename, "w", encoding="utf8") as file:
    file.write(template.format(div=div))
    print(f"Created {filename}")


# pages = []
# filename = f'../paginated abstract list/studies_ece.html'
# with open(filename, "w", encoding="utf8") as file:
#     file.write(template.format(**pages))
#     print(f"Created {filename}")