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

  <title>Appreciate 2023</title>

  <!-- Bootstrap core CSS -->
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link rel="shortcut icon" href="../assets/images/tab.png" type="image/x-icon">

  <!-- Additional CSS Files -->
  <link rel="stylesheet" href="../assets/css/fontawesome.css">
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
                  <a href=""><li class="active">All Studies</li></a>
                  <a href="ece/studies_ece.html"><li>ECE</li></a>
                  <a href="ee/studies_ee.html"><li>EE</li></a>
                  <a href="ce/studies_ce.html"><li>CE</li></a>
                  <a href="me/studies_me.html"><li>ME</li></a>
                </ul>
              </div>
            </div>
            
            <div class="col-lg-12">
              <div class="row grid">
                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_1}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_1}">
                        <h4>{title_1}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_1}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_2}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_2}">
                        <h4>{title_2}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_2}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_3}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_3}">
                        <h4>{title_3}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_3}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_4}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_4}">
                        <h4>{title_4}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_4}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_5}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_5}">
                        <h4>{title_5}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_5}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_6}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_6}">
                        <h4>{title_6}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_6}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_7}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_7}">
                        <h4>{title_7}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_7}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_8}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_8}">
                        <h4>{title_8}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_8}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_9}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_9}">
                        <h4>{title_9}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_9}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-lg-12">
              <div class="pagination">
                {buttons}
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
  <script src="../assets/js/isotope.js"></script>
  <script src="../assets/js/video.js"></script>
  <script src="../assets/js/slick-slider.js"></script>
  <script src="../assets/js/custom.js"></script>

</body>

</html>
"""


template_last = """
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
  <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link rel="shortcut icon" href="../assets/images/tab.png" type="image/x-icon">

  <!-- Additional CSS Files -->
  <link rel="stylesheet" href="../assets/css/fontawesome.css">
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
            
            <div class="col-lg-12">
              <div class="row grid">
                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_1}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_1}">
                        <h4>{title_1}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_1}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_2}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_2}">
                        <h4>{title_2}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_2}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_3}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_3}">
                        <h4>{title_3}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_3}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 templatemo-item-col all soon">
                  <div class="meeting-item">
                    <div class="thumb">
                      <div class="price">
                      </div>
                      <a href="{study_4}"><img src="../assets/images/appreciate-2023-logo.jpg" alt=""></a>
                    </div>
                    <div class="down-content">
                      <div class="date">
                      </div>
                      <a href="{study_4}">
                        <h4>{title_4}...</h4>
                      <p style="margin: 0 auto; text-align: left;">{abstract_4}...
                      <p>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-lg-12">
              <div class="pagination">
                {buttons}
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
  <script src="../assets/js/isotope.js"></script>
  <script src="../assets/js/video.js"></script>
  <script src="../assets/js/slick-slider.js"></script>
  <script src="../assets/js/custom.js"></script>

</body>

</html>
"""















first = """
                <ul>
                  <li><a class="active" href="{current_link}">{current_num}</a></li>
                  <li><a href="{next_link}"><i class="fa fa-angle-right"></i></a></li>
                </ul>
"""

mid = """
                <ul>
                <li><a href="{previous_link}"><i class="fa fa-angle-left"></i></a></li>
                  <li class="active"><a href="{current_link}">{current_num}</a></li>
                  <li><a href="{next_link}"><i class="fa fa-angle-right"></i></a></li>
                </ul>
"""

last = """
                <ul>
                <li><a href="{previous_link}"><i class="fa fa-angle-left"></i></a></li>
                  <li class="active"><a href="{current_link}">{current_num}</a></li>
                </ul>
"""

codes = []
titles = []
abstracts = []
import random
with open(r'studies.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    count = 0
    for row in reader:
        count += 1
        code = row['code']
        title = row['title'][:45]
        abstract = row['abstract_raw'][:60]
        codes.append(code)
        titles.append(title)
        abstracts.append(abstract)
    print(count)
# random.shuffle(codes)

page_counter = 1
for i in range(0, len(codes), 9):
    
    sublist = codes[i:i+9]
    # print(i)
    studies_ = []
    titles_ = []
    abstracts_ = []
    for index in range(len(sublist)):
        # print(index)
        
        study = f'../abstracts/{codes[i+index]}.html'
        title = f'{titles[i+index]}'
        abstract = f'{abstracts[i+index]}'
        print(study, title, abstract)
        studies_.append(study)
        titles_.append(title)
        abstracts_.append(abstract)

    if i == 0:
        next_link = f'../paginated abstract list/studies_{page_counter+1}.html'
        current_link = f'../paginated abstract list/studies_{page_counter}.html'
        current_num = f'{page_counter}'
        button = first.format(next_link=next_link, current_link=current_link, current_num=current_num)
        
    elif i < 144:
        previous_link = f'../paginated abstract list/studies_{page_counter-1}.html'
        next_link = f'../paginated abstract list/studies_{page_counter+1}.html'
        current_link = f'../paginated abstract list/studies_{page_counter}.html'
        current_num = f'{page_counter}'
        button = mid.format(next_link=next_link,previous_link=previous_link, current_link=current_link, current_num=current_num)
    else:
        previous_link = f'../paginated abstract list/studies_{page_counter-1}.html'
        current_link = f'../paginated abstract list/studies_{page_counter}.html'
        current_num = f'{page_counter}'
        button = last.format(previous_link=previous_link, current_link=current_link, current_num=current_num)



        filename = f'../paginated abstract list/studies_{page_counter}.html'
        with open(filename, "w", encoding="utf8") as file:
            file.write(template_last.format(
                study_1=studies_[0], title_1=titles_[0], abstract_1=abstracts_[0],
                study_2=studies_[1], title_2=titles_[1], abstract_2=abstracts_[1],
                study_3=studies_[2], title_3=titles_[2], abstract_3=abstracts_[2],
                study_4=studies_[3], title_4=titles_[3], abstract_4=abstracts_[3],
                # study_5=studies_[4], title_5=titles_[4], abstract_5=abstracts_[4],
                # study_6=studies_[5], title_6=titles_[5], abstract_6=abstracts_[5],
                # study_7=studies_[6], title_7=titles_[6], abstract_7=abstracts_[6],
                # study_8=studies_[7], title_8=titles_[7], abstract_8=abstracts_[7],
                # study_9=studies_[8], title_9=titles_[8], abstract_9=abstracts_[8],
                buttons=button,
                                    ))
            print(f"Created {filename}")
            page_counter += 1
            break






    filename = f'../paginated abstract list/studies_{page_counter}.html'
    with open(filename, "w", encoding="utf8") as file:
        file.write(template.format(
            study_1=studies_[0], title_1=titles_[0], abstract_1=abstracts_[0],
            study_2=studies_[1], title_2=titles_[1], abstract_2=abstracts_[1],
            study_3=studies_[2], title_3=titles_[2], abstract_3=abstracts_[2],
            study_4=studies_[3], title_4=titles_[3], abstract_4=abstracts_[3],
            study_5=studies_[4], title_5=titles_[4], abstract_5=abstracts_[4],
            study_6=studies_[5], title_6=titles_[5], abstract_6=abstracts_[5],
            study_7=studies_[6], title_7=titles_[6], abstract_7=abstracts_[6],
            study_8=studies_[7], title_8=titles_[7], abstract_8=abstracts_[7],
            study_9=studies_[8], title_9=titles_[8], abstract_9=abstracts_[8],
            buttons=button,
                                   ))
        print(f"Created {filename}")
    page_counter += 1