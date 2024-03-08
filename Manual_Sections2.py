from Screenshots2 import take_screenshot

links=[]
xpaths=[]

links.append("https://app.goprimer.com/direct_to_page/O7oDC?redirect=false&")
curr=["//body",
      "//div[@id='gr-1']",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']"
      ]

xpaths.append(curr)

links.append("https://app.goprimer.com/direct_to_page/g4gIh?redirect=false&")
curr=["//body",
     "//div[@id='gr-1']",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']",
      "//div[@id='gr-9']"
]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/YkM8O?redirect=false&")
curr=["//body",
      "//div[@id='gr-1']",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']",
      "//div[@id='gr-10']",
      "//div[@id='gr-11']",
      "//div[@id='gr-12']",
      "//div[@id='gr-13']",
      "//div[@id='gr-14']"
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/YMosc?redirect=false&redirect=false&")
curr=["//body",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='chart']",
      "//div[@id='gr-5']",
      "//div[@id='choose']",
      "//div[@id='chooseDesktop']",
      "//div[@id='chooseMobile']",
      "//div[@id='gr-9']",
      "//div[@id='gr-10']",
      "//div[@id='gr-11']"
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/A8WKX?redirect=false&")
curr=["//body",
      "//div[@id='titlebar']",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/EwboD?redirect=false&")
curr=["//body",
      "//div[@id='gr-1']",
      "//div[@id='Q1']",
      "//div[@id='Q2']",
      "//div[@id='Q3']",
      "//div[@id='Q4']",
      "//div[@id='Q5']",
      "//div[@id='Q6']",
      "//div[@id='success']",
      "//div[@id='gr-9']",
      "//div[@id='gr-10']",
      "//div[@id='gr-11']"
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/ulr2O?redirect=false&")
curr=["//body",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']",
      "//div[@id='gr-10']",
      "//div[@id='gr-11']",
      "//div[@id='gr-12']",
      "//div[@id='gr-13']",
      "//div[@id='gr-14']",
      "//div[@id='gr-15']",
      "//div[@id='gr-16']",
      "//div[@id='gr-17']"
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/WZBLj?redirect=false&redirect=false&")
curr=["//body",
      "//div[@id='floating']"
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']",
      "//div[@id='gr-9']",
      "//div[@id='gr-10']"
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/MMbKf?redirect=false&redirect=false&")
curr=["//body",
      "//div[@id='gr-1']",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/8gtEH?redirect=false&")
curr=["//body",
      "//div[@id='gr-1']",
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']",
      "//div[@id='gr-9']",
      "//div[@id='gr-10']",
      "//div[@id='gr-11']",
      ]
xpaths.append(curr)

links.append("https://try.goprimer.com/direct_to_page/EC23W?redirect=false&")
curr=["//body",
      "//div[@id='floating']"
      "//div[@id='gr-2']",
      "//div[@id='gr-3']",
      "//div[@id='gr-4']",
      "//div[@id='gr-5']",
      "//div[@id='gr-6']",
      "//div[@id='gr-7']",
      "//div[@id='gr-8']",
      "//div[@id='gr-9']",
      "//div[@id='gr-10']"
      ]
xpaths.append(curr)

n=0

for link in links:
    take_screenshot(link,xpaths[n],n)
    n+=1





