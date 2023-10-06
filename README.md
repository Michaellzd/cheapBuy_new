



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5645496.svg)](https://doi.org/10.5281/zenodo.5645496)
[![codecov](https://codecov.io/gh/anshulp2912/cheapBuy/branch/main/graph/badge.svg?token=WO5GVXOUSD)](https://codecov.io/gh/anshulp2912/cheapBuy)
[![Python Style Checker](https://github.com/freakleesin/cheapBuy/actions/workflows/style_checker.yml/badge.svg)](https://github.com/freakleesin/cheapBuy/actions/workflows/style_checker.yml)
[![Run Tests On Push](https://github.com/anshulp2912/cheapBuy/actions/workflows/unit_test.yml/badge.svg)](https://github.com/freakleesin/cheapBuy/actions/workflows/unit_test.yml)
[![Lint Python](https://github.com/freakleesin/cheapBuy/actions/workflows/main.yml/badge.svg)](https://github.com/anshulp2912/cheapBuy/actions/workflows/main.yml)
[![Running Code Coverage](https://github.com/anshulp2912/cheapBuy/actions/workflows/code_cov.yml/badge.svg)](https://github.com/freakleesin/cheapBuy/actions/workflows/code_cov.yml)



<!--Badges-->
<a href="https://github.com/freakleesin/cheapBuy/blob/main/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/freakleesin/cheapBuy?style=flat-square" alt="cheapBuy license" />
    
</a>
<a href="https://github.com/freakleesin/cheapBuy/fork" target="blank">
<img src="https://img.shields.io/github/forks/freakleesin/cheapBuy?style=flat-square" alt="cheapBuy forks"/>
</a>
<a href="https://github.com/freakleesin/cheapBuy/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/freakleesin/cheapBuy?style=flat-square" alt="gcheapBuy stars"/>
</a>
<a href="https://github.com/freakleesin/cheapBuy/issues" target="blank">
<img src="https://img.shields.io/github/issues/freakleesin/cheapBuy?style=flat-square" alt="cheapBuy issues"/>
</a>
<a href="https://github.com/freakleesin/cheapBuy/issues" target="blank">
<img src="https://img.shields.io/github/issues-closed/freakleesin/cheapBuy" alt="cheapBuy issues closed"/>
</a>
<a href="https://github.com/freakleesin/cheapBuy/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/anshulp2912/cheapBuy?style=flat-square" alt="cheapBuy pull-requests"/>
</a>
<a href="https://github.com/freakleesin/cheapBuy/milestones" alt="milestones">
<img src="https://img.shields.io/github/milestones/all/freakleesin/cheapBuy" /></a> 
<a href="https://github.com/freakleesin/cheapBuy/graphs/commit-activity" alt="commit activity">
<img src="https://img.shields.io/github/commit-activity/w/freakleesin/cheapBuy" /></a> 
<a href="https://img.shields.io/github/repo-size/freakleesin/cheapBuy" alt="repo size">
<img src="https://img.shields.io/github/repo-size/freakleesin/cheapBuy" /></a>



<p align="center">
    <a href="https://github.com/Michaellzd/cheapBuy_new/issues/new/choose">Report Bug</a>
   
</p>

<h1 align="center">
  cheapBuy
</h1>

## Table of Contents
- [Introduction](#Introduction)
- [Features](#Features)
- [Demo](#Demo)
- [Installation Steps](#ExecutionSteps)
- [Plan of Action](#PlanofAction)
  - [Phase 1](#Phase1)
  - [Phase 2](#Phase2)
  - [Phase 3](#Phase3)
- [License](#License)
- [Contributing](#Contributing)
- [Team Members](#TeamMember)
- [Project 2(Score cards and video)](#Proj2)
- [Acknowledgements](#Acknowledgement)

## 📖 Introduction <a name="Introduction"></a>

**cheapBuy** provides you an easy way to buy any product through your favourite website's like Amazon, Walmart, Ebay, Costco, etc, while providing prices comparison from same product from different websites. Usually, it takes lot of time to do price comparison by checking different websites. However, you can instead add our extension **cheapBuy** and it will automatically fetch you price of the same product from different websites which you can then directly compare. This extension will not only save you time, but also save you money! Overall, **cheapBuy** is an one stop solution to buy the cheapest product online.


## 🧐 Features <a name="Features"></a>
- **Price Comparison**
- **Get alternative website for the product**
- **Highlight Cheapest product**


## 🛠️ Steps of Execution <a name="ExecutionSteps"></a>

1. Clone the github repository at the preferable location in your local machine. You will need git to be preinstalled in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/Michaellzd/cheapBuy_new.git
cd cheapBuy
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of the requirements.
```
pip install -r requirements.txt
```
3. Check out the demo video to know about the use of the website in the media files.
4. To locally run the streamlit website, we would recommend setting up an Anaconda Environment and running the command
```
streamlit run cheapBuy_user_interface.py
```

## 📅 Plan of Action <a name="PlanofAction"></a>
### PHASE-1✅ <a name="Phase1"></a>
1. Fetching descirption of the user's current tab for ebay.
2. Fetching descirption of the user's current tab for Walmart.
3. Fetching descirption of the user's current tab for amazon.
4. Fetching descirption of the user's current tab for Bjs.
5. Fetching descirption of the user's current tab for Costco.
6. Web Scrapping various product details from Amazon.
7. Web Scrapping various product details from Ebay.
8. Exception handling of web scrapping.
9. Server API for web scrapping.
10. Deploying server on AWS.
11. Build an extension for this price comparison.
12. Extract knowledge like prices, sites, URL, comparison, description from scrapped data.
13. Show all the scrapped data and the knowledge gained on the extension page.

### PHASE-2 ✅ <a name="Phase2"></a>
1. Develop a website instead of extension.
2. Improvement of extension UI.
3. Highlight the cheapest option available.
4. Code restructuring.
5. Improve accuracy of the product. Example : If user's current tab is having Television of a particular brand and there is a better option available at a cheaper or comparable rate than provide alternative product accordingly.
6. Web Scrapping various product details from Walmart.
7. Web Scrapping various product details from Costco.
8. Web Scrapping various product details from BJs.
9. Improve code execution speed using multithreading.

### PHASE-3 ✅ <a name="Phase3"></a>
1. Fetching descirption of the user's current tab for Bestbuy.
2. Fetching descirption of the user's current tab for Trader Joes.
3. Fetching descirption of the user's current tab for Kroger.
4. Web Scrapping various product details from Bestbuy.
5. Web Scrapping various product details from Trader Joes.
6. Web Scrapping various product details from Kroger.
7. Improve code execution speed using multiprocessing.
8. Improve website UI.
9. Add sidebar.
10. Users can choose the selected website and price range.
11. Improve the accuracy of searching products.
12. Link buttons for all websites.

### PHASE-4 ⌛ <a name="Phase3"></a>
1. Automatic deployment of server using Teraform or ansible.
2. Dashboard including how many user's click on the website.
3. Email notification of the available coupon to the user.
4. Alternate product suggestion feature.
5. Show a available coupon on other shopping website.
6. Add more websites webScrapping .

🌟 You are all set! 🌟

## 📝 License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/anshulp2912/cheapBuy/blob/main/LICENSE) for more details.

## 🍰 Contributing <a name="Contributing"></a>
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/anshulp2912/cheapBuy/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## 👥 Team Members(Group 30) <a name="TeamMember"></a>
Jack Hou	

Zhendong Lu	

Feng Wang

Enxi Zhang

## Project 2(Score card and video!) <a name="Proj2"></a>
<span style="color:blue">[Project 2 Readme !](proj2/Readme.md)</span>


## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank all the teaching assistants for their support throughout the project.
We would also like to extend our gratitude to previous group : https://github.com/rliu9/cheapBuy
- [https://streamlit.io/](https://streamlit.io/)
<br>
