Source for Scaling Up

## 1k recored

Root-mean-square error (RMSE) = 3.0568349308077423
Mean Absolute Error (MAE) = 2.557977944612503
Hit Rate (HR) = 0.0005270092226613965
Cumulative Hit Rate (cHR) = 0.0005270092226613965
Average Reciprocal Hit Rate (ARHR) = 0.00013065436978480457
Coverage = 0.8481012658227848
Diversity = 0.017654808959156786
Novelty = 2.238268909550851

Top 10 recommendations:
Artec Textureline Smoothing Serum, 8.4-Ounce Pump (Pack of 2)
Hilary Duff With Love Eau de Parfum
Exuviance - Rejuvenating Treatment Masque
MACKIE For Women By BOB MACKIE Eau De Toilette Spray
Sisley Phyto Teint Eclat
KINeSYS Spray-On Sunscreen, SPF 30, Fragrance-Free, 1 fl oz(30 ml) (Pack of 2)
Komenuka Bijin 10-Product Trial/Sample Set from Rice Bran
NeoStrata Bionic Face Cream PHA 12
Pravana Sulfate-Free Volumizing Shampoo 33.7oz
John Allan's Sport, Conditioning Shampoo 12.6 fl oz (375 ml)

Thử tunning lại:
als = ALS(maxIter=20, regParam=0.5, rank=20, userCol="userIdIndex", itemCol="productIdIndex", ratingCol="rating",
coldStartStrategy="drop")

Root-mean-square error = 2.01463887934963  
Top 10 recommendations:  
Artec Textureline Smoothing Serum, 8.4-Ounce Pump (Pack of 2)
Scannon Ghost Deep Night Eau de Toilette
L'oreal Professionnel Serie Expert Power Dose Color (15 Vials with Pump)
Revlon Frost & Glow Highlighting Kit 1 ea
Dr. Ohhira's Probiotic Magoroku Skin Care Treatment ProFormula - 1 - Tube
Poshe Anti-Microbial Basecoat 0.5oz
Vidal Sassoon Salon Pro VS756R 1600Watt Wall Mount Hair Dryer
Alison Raffaele Blotting Tissues
Soft 'N Style 1-1/2" Jumbo Black Foam Roller (8 Per Bag) (Pack of 6 bags)
Earth Mama-Angel Baby VBAC Preparation, 1 cd
Total time for recommending top N: 3.4277029037475586 seconds
Memory usage: 100.68359375 MB

# Tập 10k record

Cho chạy dò tham số:

Kết quả:
Best parameters: rank=30, maxIter=20, regParam=0.1

RMSE score = 1.7022076868809926 MAE score = 0.8878960800816615 Rsquared score = -0.9161540103248658 Explained Variance score = -0.7279929500564275
Top 10 recommendations:  
Bare Escentuals bareMinerals Blush
Venom Gloss
Derma e Complete E Cranberry Creme, Intense Moisturizing Formula- Creme Hydrante, 2 oz (Pack of 2)
Barielle Intensive Nail Renewal Oil .50 Fl.Oz.
Thymes Bath Salts Envelope (2 oz)
Komenuka Bijin 10-Product Trial/Sample Set from Rice Bran
Ahava Mens Deep Cleansing Gel, 3.4oz
Ahava Mens Protective Moisturizing Fluid SPF 15, 1.7oz
Healthy Sexy Hair Soy Paste Texture Pomade (1.8oz)
American Crew Grooming Creme for Men, 3.53-Ounce Jars (Pack of 2)
Total time for recommending top N: 3.35653018951416 seconds
Memory usage: 89.23046875 MB

# Tập 100k record

Kết quả với tham số đã tuning phía trên:

Mean Absolute Error (MAE) = 1.0386897842444986  
Calculate RMSE
Root-mean-square error (RMSE) = 2.0488968935023872  
Top 10 recommendations:
Artec Textureline Smoothing Serum, 8.4-Ounce Pump (Pack of 2)
Wella Color Charm Liquid #435/5g Light Golden Brown Haircolor
Prestige Revitalizing Cream - 50ml/1.7oz
SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g
Dial Daily Care Antibacterial Hand Soap , 7.5 fl oz (221 ml)
Casran Cologne by Chopard for men Colognes
Opium 1.6oz. Eau de Parfum Spray for Women by Yves Saint Laurent
Kenneth Cole Black By Kenneth Cole For Women. Set-eau De Parfum Spray 1.7 OZ & Body Lotion 3.4 OZ & Shower Gel 3.4 OZ
Tweezerman Chrome Cuticle Nipper 1/4 Jaw 3255-R
Cricket Static Free Fast Flo Vent Brush
Total time for recommending top N: 3.074472188949585 seconds
Memory usage: 100.57421875 MB

### Full tập 200k record

RMSE score = 2.2256901896972496 MAE score = 1.3276668848043172 Rsquared score = -2.1208552176544297 Explained Variance score = -1.2044114239996988

Top 10 recommendations:  
Kiss My Face Pore Shrink Deep Pore Cleansing Mask  
Avalon Organics CoQ10 Facial Cleansing Creme  
Dove Sensitive Essentials Cleansing Cloths, Refill, 30 Count  
Komenuka Bijin Premium Hair Care Set: Moisturizing Hair Shampoo & Hair Treatment / Conditioner
Burt's Bees Pore Refining Mask with French Green Clay, 1-Ounce Jar  
Komenuka Bijin 10-Product Trial/Sample Set from Rice Bran  
Burt's Bees Burt's Bees Milk & Honey Body Lotion Naturally Nourishing  
Mini Lotion Kit - 1 oz./3 bottle  
Bliss Diamancel Diamond Tough Foot Buffer No.11, Medium  
Venom Gloss

Total time for recommending top N: 37.612921476364136 seconds
Memory usage: 114.25 MB
