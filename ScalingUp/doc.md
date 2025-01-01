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
Root-mean-square error = 2.0832469749998226

Top 10 recommendations:  
Artec Textureline Smoothing Serum, 8.4-Ounce Pump (Pack of 2)
One with Nature Almond Bar Soap
Ahava Mineral Eye Cream, 1oz
Banana Boat Faces Plus Waterproof Sunscreen Stick SPF#30 16 ml
PHEROSE by Realm - Gift Set for Women
Natura Bisse Dry Skin Milk
Paraffin Wax Refill With Heat Retaining Capacity
Tri Structural Balance...NEW Hydrating Reconstructor 6oz
NUXE Reve de Miel Family Balm-1.7 oz.
Pevonia Evolutive Eye Cream - Ligne Yeux
Total time for recommending top N: 2.9230191707611084 seconds
Memory usage: 94.6015625 MB

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

Calculating metrics...
Mean Absolute Error (MAE) = 1.0386897842444986  
Calculate RMSE
Root-mean-square error (RMSE) = 2.0488968935023872

Top 10 recommendations:  
Steam Facial By Kaz  
Derma e Pycnogenol Gel with Vitamins C E & A  
Derma e Pycnogenol Eye Gel With Green Tea Extract  
Coco by Chanel for Women. 1.7 Oz Eau De Toilette Spray  
100% Unrefined Certified Grade A Shea Butter with a Hint of Organic Lavender Essential Oil 4 oz. By AAA Shea Butter
Zum Rub Body Moisturizer Lavender-Mint -- 2.5 oz  
BLINC KISS ME MASCARA  
Refinity Rejuvenating Hydrogel - 15% AHA 2 fl oz.  
Refinity Rejuvenating Lotion 2 oz  
The Body Shop Lip Liner Fixer

Total time for recommending top N: 44.94420886039734 seconds
Memory usage: 96.91796875 MB

Mặc dù chạy rất nhanh nhưng điểm số không được cao cho lắm mặc dù đã tuning
