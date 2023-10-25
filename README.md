<h1 align="center">
  cheapBuy_New
</h1>



[![DOI](https://zenodo.org/badge/701486893.svg)](https://zenodo.org/badge/latestdoi/701486893)
![Code Linting](https://github.com/Michaellzd/cheapBuy_new/workflows/Code%20Linting/badge.svg)
![Static Badge](https://img.shields.io/badge/black-black.svg?label=Code%20formatters)
![Static Badge](https://img.shields.io/badge/flake-blue.svg?label=Style%20Checkers)
![Static Badge](https://img.shields.io/badge/flake-redl.svg?label=Syntax%20Checkers)
[![codecov](https://codecov.io/gh/anshulp2912/cheapBuy/branch/main/graph/badge.svg?token=WO5GVXOUSD)](https://codecov.io/gh/anshulp2912/cheapBuy)



<!--Badges-->
<a href="https://github.com/freakleesin/cheapBuy/blob/main/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/freakleesin/cheapBuy?style=flat-square" alt="cheapBuy license" />
    
</a>
<a href="https://github.com/Michaellzd/cheapBuy_new/fork" target="blank">
<img src="https://img.shields.io/github/forks/Michaellzd/cheapBuy_new?style=flat-square" alt="cheapBuy forks"/>
</a>
<a href="https://github.com/Michaellzd/cheapBuy_new/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/freakleesin/cheapBuy?style=flat-square" alt="gcheapBuy stars"/>
</a>
<a href="https://github.com/Michaellzd/cheapBuy_new/issues" target="blank">
<img src="https://img.shields.io/github/issues/Michaellzd/cheapBuy_new?style=flat-square" alt="cheapBuy issues"/>
</a>
<a href="https://github.com/freakleesin/cheapBuy/issues" target="blank">
<img src="https://img.shields.io/github/issues-closed/Michaellzd/cheapBuy_new" alt="cheapBuy issues closed"/>
</a>
<a href="https://github.com/Michaellzd/cheapBuy_new/graphs/commit-activity" alt="commit activity">
<img src="https://img.shields.io/github/commit-activity/w/Michaellzd/cheapBuy_new" /></a> 
<a href="https://img.shields.io/github/repo-size/Michaellzd/cheapBuy_new" alt="repo size">
<img src="https://img.shields.io/github/repo-size/Michaellzd/cheapBuy_new" /></a>



<p align="center">
    <a href="https://github.com/Michaellzd/cheapBuy_new/issues/new/choose">Report Bug</a>
</p>


## Table of Contents
- [Introduction](#Introduction)
- [Features](#Features)
- [Installation Steps](#ExecutionSteps)
- [Project 2 (Score cards and video)](#Proj2)
- [Roadmap](#Roadmap)
- [Team Members](#TeamMember)
- [License](#License)
- [Contributing](#Contributing)
- [Acknowledgements](#Acknowledgement)
- [Contact Us](#Contact)


## 📖 Introduction <a name="Introduction"></a>

**cheapBuy** provides you an easy way to buy any product through your favourite website's like Amazon, Walmart, Ebay, Costco, etc, while providing prices comparison from same product from different websites. Usually, it takes lot of time to do price comparison by checking different websites. However, you can instead add our extension **cheapBuy** and it will automatically fetch you price of the same product from different websites which you can then directly compare. This extension will not only save you time, but also save you money! Overall, **cheapBuy** is an one stop solution to buy the cheapest product online.


## 🧐 Features <a name="Features"></a>
- **Price Comparison**
- **Get alternative website for the product**
- **Highlight Cheapest product**
- **Send Cheapest product to users' emails**
- **Regularly crawl information and send desired products to customers via email.**
- **Cancel anytime easily with the email service.** 




## 🛠️ Steps of Execution <a name="ExecutionSteps"></a>

1.Clone the github repository at the preferable location in your local machine. You will need git to be preinstalled in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/Michaellzd/cheapBuy_new.git
```
2.This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of the requirements.
```
pip install -r requirements.txt
```
3.Register an account at mailgun. And applied an API key and use in in mailgun.py [Mailgun](https://www.mailgun.com/) 
 
4.Check out the demo video to know about the use of the website in the media files.

5.To locally create a database to store users'info and url, we would recommend setting up an Anaconda Environment and running the command
```
python db.py
```

6.To locally run the streamlit website, we would recommend setting up an Anaconda Environment and running the command
```
streamlit run cheapBuy_user_interface.py
```

7.To locally run the Scheduled Information Crawling and Email Sending Service, we would recommend running the command
```
python scheduler.py
```
## 📝 Project 2(Score card and video!) <a name="Proj2"></a>
<span style="color:blue">[Project 2 Readme !](proj2/README.md)</span>

## 🗺️ Roadmap <a name="Roadmap"></a>

### Phase 1: Planning and Research

#### Market Research and Analysis
- Identify the target audience and their needs.
- Analyze competitors and similar browser extensions.
- Determine potential revenue streams and business models.

#### Feature Definition
- Finalize the list of features based on research.
- Prioritize features based on their importance and feasibility.

#### Technology Stack Selection
- Choose the technology stack for extension development.
- Set up development environments and tools.

### Phase 2: Development

#### Core Functionality Development
- Develop the extension's core functionality for price comparison.
- Implement the ability to fetch product prices from different websites.

#### Website Integration
- Integrate with popular e-commerce websites like Amazon, Walmart, eBay, Costco, etc.
- Implement web scraping and data retrieval mechanisms.

#### User Interface Design
- Design a user-friendly interface for the extension.
- Ensure a seamless user experience during price comparison.

#### Email Integration
- Develop the feature to send the cheapest product information to users' emails.

### Phase 3: Testing
- Testing and Quality Assurance
- Conduct extensive testing to identify and fix bugs.
- Ensure compatibility with various web browsers.

### Phase 4: Launch

#### Soft Launch and User Feedback
- Users can run the project.
- Gather user feedback and make necessary improvements.


### Phase 5: Post-Launch

#### Monitoring and Maintenance
- Continuously monitor the extension's performance and user feedback.
- Regularly update the extension to fix issues and add new features.

#### Regular Data Crawling
- Set up a system for regular data crawling to keep prices up-to-date.
- Implement mechanisms to handle changes in website structures.

#### User-Requested Product Alerts (4 weeks)
- Develop a feature that allows users to request alerts for specific products.
- Send alerts to users' emails when desired products meet their specified criteria.


### Phase 6: Scaling and Growth

#### Expansion (Ongoing)
- Post it online.
- Consider expanding to more e-commerce websites and markets.
- Explore partnerships with retailers for data access.

#### Mobile App Integration (8 weeks)
- Develop a mobile app version of cheapBuy for a broader user base.

#### User Engagement and Marketing (Ongoing)
- Continuously work on user engagement and marketing strategies to grow the user base.



## 👥 Team Members <a name="TeamMember"></a>
Group 30:

Jack Hou	

Zhendong Lu	

Feng Wang

Enxi Zhang


## 📝 License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/anshulp2912/cheapBuy/blob/main/LICENSE) for more details.

## 🍰 Contributing <a name="Contributing"></a>
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/anshulp2912/cheapBuy/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank all the teaching assistants for their support throughout the project.
We would also like to extend our gratitude to previous group : https://github.com/rliu9/cheapBuy
- [https://streamlit.io/](https://streamlit.io/)
<br>


## 📇 Contact US <a name="Contact"></a>

For any inquiries, you can reach out to us via email:

- [735955506@qq.com](mailto:1.735955506@qq.com)
- [fwang32@ncsu.edu](mailto:fwang32@ncsu.edu)
- [yhou8@ncsu.edu](mailto:yhou8@ncsu.edu)
- [1gabriel.zhang1@gmail.com](mailto:1gabriel.zhang1@gmail.com)

## 🪧 Poster
![Poster](media/poster.png)
