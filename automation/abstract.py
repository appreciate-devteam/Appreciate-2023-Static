import csv

template = """
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="Template Mo">
  <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900" rel="stylesheet">

  <title>Abstract: {code}</title>

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link rel="shortcut icon" href="../assets/images/tab.png" type="image/x-icon">

  <!-- Additional CSS Files -->
  <link rel="stylesheet" href="./assets/css/fontawesome.css">
  <link rel="stylesheet" href="../assets/css/templatemo-edu-meeting.css">
  <link rel="stylesheet" href="../assets/css/owl.css">
  <link rel="stylesheet" href="../assets/css/lightbox.css">
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
            <a href="../index.html" class="logo">
              2023 | APPRECIATE
            </a>
            <!-- ***** Logo End ***** -->
            <!-- ***** Menu Start ***** -->
            <ul class="nav">
              <li><a href="../index.html">Home</a></li>
              <li><a href="../paginated abstract list/main_abstract_list.html" class="active">Studies</a></li>
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
          <h6>TUP - MANILA</h6>
          <h2>COLLEGE OF ENGINEERING</h2>
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
              <div class="meeting-single-item">
                <div class="thumb">
                  <div class="price">

                  </div>

                <img src="../assets/images/studies-temp.jpg" alt="">
                </div>
                <div class="down-content">
                  <!-- <a href="meeting-details.html"> -->
                    <h4>{title}</h4>
                  <!-- </a> -->
                  <p>{proponents}</p>
                  <p class="description">
                    {abstract}
                  </p>

                  <p>{sdg}</p>

                  <div class="col-lg-12">

                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-12">
            <div class="main-button-red">
              <a href="../paginated abstract list/main_abstract_list.html">Back To Studies List</a>
            </div>
          </div>
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
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <script src="../assets/js/isotope.min.js"></script>
  <script src="../assets/js/owl-carousel.js"></script>
  <script src="../assets/js/lightbox.js"></script>
  <script src="../assets/js/tabs.js"></script>
  <script src="../assets/js/video.js"></script>
  <script src="../assets/js/slick-slider.js"></script>
  <script src="../assets/js/custom.js"></script>
  
</body>

</html>
"""

with open(r'studies.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        code = row['code']
        title = row['title']
        proponents = row['proponents']
        abstract = row['abstract_raw']
        sdg = row['sdg']
        print(code)

        filename = f'../abstracts/{code}.html'
        with open(filename, "w", encoding="utf8") as file:
            file.write(template.format(code=code, title=title, proponents=proponents, abstract=abstract, sdg=sdg))
            print(f"Created {filename}")
