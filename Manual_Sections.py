from selenium import webdriver
from screenshot import take_screenshot
links=[]
xpaths=[]

links.append("https://magicspoon.com/pages/treatslpv1")
curr=["//body",
      "//div[@class='builder-block builder-8aca611232e04625b2fa2a0c7d51582a builder-has-component css-qbeeke']",
      "//div[@class='builder-block builder-eff36eb10ff8443d98aa8a93af8f8f34 builder-has-component css-lbzqk9']",
      "//div[@class='builder-block builder-23bb8d78dfbb4cb994270c1fa7983ced css-77igky']",
      "//div[@class='builder-block builder-add0b92a250f4ab78d829726a8282a4b builder-has-component css-j6qqa2']",
      "//div[@builder-id='builder-967d1d6025ea4666b5e1165487112376']",
      "//div[@builder-id='builder-82bd5d03ad6d4fa1b0b0c1a52822e58e']",
      "//footer"]

xpaths.append(curr)

links.append("https://get.drsquatch.com/treat-yo-self-a/?utm_source=tiktok&utm_medium=paid&utm_campaign=__CAMPAIGN_ID__&utm_content=__AID__&utm_term=__CID__&nb_platform=tiktok&nbt=nb%3Atiktok%3A%3A__CAMPAIGN_ID__%3A__AID__%3A__CID__")
curr=["//body",
      "//div[@id='lp-pom-block-11-color-overlay']",
      "//div[@id='lp-pom-block-24-color-overlay']",
      "//div[@id='lp-pom-block-860-color-overlay']",
      "//div[@id='lp-pom-block-971-color-overlay']",
      "//div[@id='lp-pom-block-377-color-overlay']",
      "//div[@id='lp-pom-block-900-color-overlay']",
      "//div[@id='lp-pom-block-845-color-overlay']",
      "//div[@id='lp-pom-block-863-color-overlay']",
      "//div[@id='lp-pom-block-809-color-overlay']",
      "//div[@id='lp-pom-block-841-color-overlay']"]
xpaths.append(curr)

links.append("https://www.briogeohair.com/?utm_source=tiktok&utm_medium=tiktok&utm_campaign=abbyboostingbfcm")
curr=["//body",
      "//div[@class='bg-quinary-2 text-grey-1 relative z-[2000] flex items-center justify-center px-3 py-[6px] md:py-[9px]']",
      "//div[@class='items-center1 relative z-0 flex justify-between py-4 px-4 md:px-12 lg:py-5']",
      "//section[@data-comp='hero']",
      "//section[@id='productRecommendations-0186901d-87d2-716f-8bff-589f96cfa7da']",
      "//div[@id='ImageWithText-0186901d-8c4c-71aa-91a9-bb4f9191ab79']",
      "//section[@data-comp='category-carousel']",
      "//section[@data-comp='product-spotlight']",
      "//section[@data-comp='four-up-cta']",
      "//section[@data-comp='BorderedGrid']",
      "//div[@id='ImageWithText-0186a8d3-c8c1-74e0-9834-4c1618236079']",
      "//footer[@class='bg-black']//a[@class='w-[32px] md:w-[48px]']"
      ]
xpaths.append(curr)

links.append("https://www.jonesroadbeauty.com/pages/the-platinum-pink-kit-2023?&nb_platform=tiktok&nbt=nb%3Atiktok%3A%3A__CAMPAIGN_ID__%3A__AID__%3A__CID__")
curr=["//body",
      "//div[@class='r-192nbk1']",
      "//div[@class='r-5un752']",
      "//div[@class='r-1hvdloo']",
      "//div[@data-rid='d1e13c5d-d620-4a4a-8a1b-b9b349130316']",
      "//div[@class='r-jcilla']",
      "//div[@class='r-110wlzy']",
      "//div[@class='r-2zip2c']",
      "//div[@class='r-o66o4d']",
      "//div[@class='r-1oq9hxu']",
      "//footer[@class='footer']"
      ]
xpaths.append(curr)

links.append("https://www.carawayhome.com/collections/?utm_source=tiktok&utm_medium=paidsocial&utm_campaign=prospecting&utm_term=caraway&utm_product=multi&utm_color=cream")
curr=["//body",
      "//div[@class='css-zvd0tq']",
      "//nav[@class='css-14ekgll']",
      "//section[@class='css-13gtag6']",
      "//div[@class='css-i49a56']",
      "//div[@class='css-1c8246u']",
      "//section[@id='cookware']",
      "//section[@id='stainless-steel-cookware']",
      "//section[@id='bakeware']",
      "//section[@id='food-storage']",
      "//section[@id='prepware']",
      "//section[@id='tea-kettle']",
      "//section[@id='bundles']",
      "//section[@id='linens']",
      "//section[@id='accessories']",
      "//footer"
      ]
xpaths.append(curr)

links.append("https://www.olly.com/pages/adaptogens")
curr=["//body",
      "//header[@id='header']",
      "//div[@id='s-58e9013b-1fcc-4895-837f-dabec5271a40']",
      "//div[@id='s-4c3ffbca-de49-491c-8ae2-54168ad7e08a']",
      "//div[@id='s-ad2cc388-82a9-49d0-932c-65b9ba84371a']",
      "//div[@id='s-6cdd75e3-16e5-4bb9-9e84-75a0c4e893a3']",
      "//div[@id='s-fbfca818-e960-4bda-89a5-9f137d38683c']",
      "//div[@id='s-e864078b-ad97-4b0e-b00d-97f9718a9c30']",
      "//div[@id='shopify-section-footer']",
      ]
xpaths.append(curr)

links.append("https://ridge.com/collections/the-ceramic-powder-collection/?nb_platform=tiktok&nbt=nb%3Atiktok%3A%3A__CAMPAIGN_ID__%3A__AID__%3A__CID__")
curr=["//body",
      "//header[@id='header']",
      "//div[@id='s-4eb48e59-ee0c-4bc2-916c-a74f158f161b']",
      "//div[@id='s-16d52263-6e6c-4ee3-9b51-7c85713d628d']",
      "//div[@id='s-21553bb0-03c6-426d-ab36-2a8392aaf3b8']",
      "//div[@id='s-a5556b89-b275-4e29-b4f3-de1acb9bce10']",
      "//div[@id='scrollto_collection']",
      "//div[@id='s-c9405746-0260-4f0d-92ae-542b0b7dacd2']",
      "//div[@id='s-09f877df-8755-4402-b5d9-0a05de73eecd']",
      "//div[@id='s-35bff5cb-4d6e-443b-a402-3f3683bef2a2']",
      "//div[@id='shopify-section-footer']"
      ]
xpaths.append(curr)

links.append("https://www.rarebeauty.com/pages/find-comfort-collection?utm_source=tiktok&utm_medium=paid-social&utm_campaign=prospecting")
curr=["//body",
      "//header[@id='header']",
      "//div[@id='shopify-section-template--15128357896327__ad3254cc-838e-403a-853a-bb7f7ad56326']",
      "//div[@id='shopify-section-template--15128357896327__68fc9b35-94c3-479d-b681-f163e357c0b4']",
      "//div[@id='shopify-section-template--15128357896327__926d6537-b21a-4cf1-93ed-51d7704b2241']",
      "//div[@id='shopify-section-template--15128357896327__623c73bf-9a39-4b44-9b78-77c362af545c']",
      "//div[@id='shopify-section-template--15128357896327__5758e5f6-5974-4638-86b8-bdb6c0ccf7fc']",
      "//footer"
      ]
xpaths.append(curr)

links.append("https://jolieskinco.com/products/the-jolie-showerhead?variant=41313550893213")
curr=["//body",
      "//div[@id='shopify-section-layout-header']",
      "//div[@id='shopify-section-template--22105685262629__1644420323b507d39d']",
      "//div[@id='shopify-section-template--22105685262629__16444205495538ba40']",
      "//div[@id='shopify-section-template--22105685262629__16444204404fdf364e']",
      "//div[@id='shopify-section-template--22105685262629__1644421270c3710742']",
      "//div[@id='shopify-section-template--22105685262629__1658168044191f64e8']",
      "//div[@id='shopify-section-template--22105685262629__1658169478c410ee12']",
      "//div[@id='shopify-section-template--22105685262629__165848358699323cfa']",
      "//div[@id='shopify-section-template--22105685262629__1658170745feec78e4']",
      "//div[@id='shopify-section-template--22105685262629__165817116145eb785d']",
      "//div[@id='shopify-section-template--22105685262629__16444204906e8ceedb']",
      "//div[@id='shopify-section-template--22105685262629__1644943313eb66fc11']",
      "//div[@id='shopify-section-template--22105685262629__1644420507d2411681']",
      "//div[@id='shopify-section-template--22105685262629__1645027045b3019647']",
      "//div[@id='shopify-section-template--22105685262629__1645027921ad950cf0']",
      "//div[@id='shopify-section-layout-footer']"
      ]
xpaths.append(curr)

links.append("https://goflaus.com/products/flaus-starter-kit/?gad_source=1&gclid=Cj0KCQiA2KitBhCIARIsAPPMEhI4rPUqPGVWAH-fZFJ251ea-xeb6l7EsYqUCnzdap0x8BjW73zkvZ0aAr-0EALw_wcB")
curr=["//body",
      "//header[@id='header']",
      "//section[@id='shopify-section-template--16604323872956__landing-product']",
      "//div[@id='shopify-section-template--16604323872956__video-plug']",
      "//div[@id='shopify-section-template--16604323872956__video-fam']",
      "//div[@id='shopify-section-template--16604323872956__ticker-news']",
      "//div[@id='shopify-section-template--16604323872956__dfu-feature']",
      "//section[@id='shopify-section-template--16604323872956__product-recommendation']",
      "//div[@id='shopify-section-template--16604323872956__7-reasons']",
      "//div[@id='shopify-section-template--16604323872956__8a6ca8f9-3082-4a38-bf9f-752db291e47b']",
      "//div[@id='shopify-section-template--16604323872956__hero']",
      "//div[@id='shopify-section-template--16604323872956__reviews']",
      "//div[@id='shopify-section-template--16604323872956__landing-comparison']",
      "//div[@id='product-reviews']",
      "//div[@id='shopify-section-template--16604323872956__landing-faq']",
      "//section[@id='shopify-section-template--16604323872956__product-bundles']",
      "//section[@id='shopify-section-template--16604323872956__product-also-likes']",
      "//div[@id='shopify-section-template--16604323872956__dual-column']",
      "//div[@id='shopify-section-footer']"
      ]
xpaths.append(curr)


n=0

for link in links:
    take_screenshot(link,xpaths[n],n)
    n+=1





