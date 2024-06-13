from selenium.webdriver.common.by import By
BASE_URL="https://practice.automationtesting.in/"
SHOP_LINK= (By.ID, "menu-item-40")
ELEMENT=(By.CSS_SELECTOR,"#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img")
IMAGE=(By.CSS_SELECTOR,"#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link")
ANDROID=(By.XPATH,"//*[@id='woocommerce_product_categories-2']/ul/li[1]/a")
IMAGE_ANDROID=(By.CSS_SELECTOR,"#content > ul > li > a.woocommerce-LoopProduct-link > img")
HTML=(By.CSS_SELECTOR,"#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
IMAGE_HTML=(By.CSS_SELECTOR,"#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img")
JAVASCRIPT=(By.CSS_SELECTOR,"#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-21 > a")
IMAGE_JAVASCRIPT=(By.CSS_SELECTOR,"#content > ul > li.post-165.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.product_tag-mastering.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img")
SELENIUM=(By.XPATH,"/html/body/div[1]/div[2]/div/aside/div[3]/ul/li[4]/a")
IMAGE_SELENIUM=(By.CSS_SELECTOR,"#content > ul > li > a.woocommerce-LoopProduct-link > img")
ACCOUNT=(By.CSS_SELECTOR,"#menu-item-50 > a")
MAIL=(By.ID,"reg_email")
PASSWORD=(By.ID,"reg_password")
REGISTER=(By.NAME,"register")
ALERT_MESSAGE=(By.CSS_SELECTOR,"#customer_login > div.u-column2.col-2 > form > p:nth-child(2) > div")
ALERTMESSAGE="The password should be at least seven characters long. To make it stronger, use upper and lower case letters, numbers and symbols like ! ' ? $ % ^ & )."
ERRORMESSAGE=(By.CSS_SELECTOR,"#page-36 > div > div.woocommerce > ul > li")
ERROR_MESSAGE="Please provide a valid email address."
PASSWORDALERT=(By.CSS_SELECTOR,"#page-36 > div > div.woocommerce > ul > li")
PASSWORD_ALERT="Please enter an account password."