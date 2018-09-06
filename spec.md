# Specifications

The Newshighlight project requires a prerequisite understanding of the following:

- ```Python 3.6```

- ```Flask```

## Sites that helped me create News Highlight app

- [News API](https://newsapi.org/docs/endpoints/everything)
  Got the news api

- [YouTube](www.youtube.com)
  got flask tutorials


Upon any kind of difficulties when using Newshighlight, do not hesitate to contact me at kiprotichbrian8@gmail.com


## Table of Contents ##
- [Introduction](#1-introduction)
- [System Overview](#2-system-overview)
- [Usage](#2.2-usage)
- [Future Directions and Open Questions](#2.3-future-directions-and-open-questions)


   *  **How the system works** 

  The following are the steps on how The News Web app works, (This is an error-free case.)

       Fetching data:
            Periodically, the News app gets updates from The News Web API using the defined Base_URL and an API_KEY, with the use of a context manager, the data from the API gets read, then converted into json format and stored in an object.

      Processing data:
            The Json data then gets processed while applying a filter by the key value assigned to a variable
            i.e
            urlToImage = item.get('urlToImage)
            if urlToImage:
                create object, then instantiate it respective class.
      Displaying data:
            Processed data then get passed into the template(html), where it gets iterated through and displayed.

  *  **2.2. Usage**


       **Minimum Requirements(if working on a local environment)**
    1. Fair/Good internet connection.
    2. Before Running this Project
      i. run  > pip install -r requirements.txt.

      **You can also choose to use the live link**
      Steps
    1. With a browser of your choice, Visit [https://newshighlightsapiapp.herokuapp.com/](NewsHighlightsLive)
    2. Onload, the page displays news sources(Channels").
    3. Click on any channel you woud like to read news from.
    4. You will be presented with various articles from the news source.
    5. Click any that you find interesting.
  
  * **Disclaimer**
    The data contained is not filtered by contents, hence the news app won't be responsible for any rude or unfriendly wordings or images.
        
 * **Compatibility issues**

    The app is works as expected across all platforms, incase you face any compatibility issue feel free to reach out.
      
* **2.3. Future Directions and Open Questions**

   In the discussion of future directions and open questions, it is important to remember that
   The News app has been designed to allow a large amount of flexibility for many different future use cases. This is because it is implemented using an approved Python(FLASK) app structure.
   Any suggestions and changes are welcomed
