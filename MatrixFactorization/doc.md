Source for Matrix Factorization method

RMSE: Root Mean Squared Error. Lower values mean better accuracy.
MAE: Mean Absolute Error. Lower values mean better accuracy.
HR: Hit Rate; how often we are able to recommend a left-out rating. Higher is better.
cHR: Cumulative Hit Rate; hit rate, confined to ratings above a certain threshold. Higher is better.
ARHR: Average Reciprocal Hit Rank - Hit rate that takes the ranking into account. Higher is better.
Coverage: Ratio of users for whom recommendations above a certain threshold exist. Higher is better.
Diversity: 1-S, where S is the average similarity score between every possible pair of recommendations
for a given user. Higher means more diverse.
Novelty: Average popularity rank of recommended items. Higher means more novel.

Kết quả thử nghiệm 100 record rating:
| Algorithm | RMSE | MAE | HR | cHR | ARHR | Coverage | Diversity | Novelty |
|-----------|-------|-------|-------|-------|-------|----------|-----------|---------|
| SVD - Tuned | 1.4965 | 1.1239 | 0.0244 | 0.0244 | 0.0122 | 0.9512 | 0.9860 | 15.2676 |
| SVD - Untuned | 1.5573 | 1.1706 | 0.0122 | 0.0122 | 0.0061 | 0.9878 | 0.9808 | 14.2912 |

TOP 10 Result:

- SVD Tuned:
  Liz Claiborne Curve Eau de Toilette Spray: 4.81
  Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 4.72
  Michel Design Works Bath Gift Set - Beach: 4.67
  Exuviance Multi-Protective Day Creme SPF 15: 4.65
  Glysomed Body Lotion, 8.5-Ounce Bottles: 4.59
  Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.55
  Curve Crush FOR WOMEN by Liz Claiborne - 0.50 oz EDT Spray: 4.55
  Palladio Herbal Lipstick,: 4.53
  Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.53
  SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.53

  Total time for recommending top N: 0.003542184829711914 seconds

  Memory usage: 68.82421875 MB

- SVD Untuned:
  Liz Claiborne Curve Eau de Toilette Spray: 4.76
  Exuviance Multi-Protective Day Creme SPF 15: 4.46
  Michel Design Works Bath Gift Set - Beach: 4.42
  Glysomed Body Lotion, 8.5-Ounce Bottles: 4.41
  SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.39
  Curve Crush FOR WOMEN by Liz Claiborne - 0.50 oz EDT Spray: 4.37
  Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.36
  Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.30
  Palladio Herbal Lipstick,: 4.30
  Palladio Liquid Eyeliner #262 Lavender: 4.28

  Total time for recommending top N: 0.0038051605224609375 seconds

  Memory usage: 70.4296875 MB

Kết quả thử nghiệm tập 10k record rating:

| Algorithm     | RMSE   | MAE    | HR     | cHR    | ARHR   | Coverage | Diversity | Novelty  |
| ------------- | ------ | ------ | ------ | ------ | ------ | -------- | --------- | -------- |
| SVD - Tuned   | 1.2500 | 0.9647 | 0.0047 | 0.0047 | 0.0020 | 0.9989   | 0.9951    | 154.0847 |
| SVD - Untuned | 1.2555 | 0.9857 | 0.0050 | 0.0050 | 0.0022 | 0.9998   | 0.9927    | 102.4370 |

Top 10 result:

- Tuned:
  Liz Claiborne Curve Eau de Toilette Spray: 5.00
  Basis Cleaner Clean Face Wash, 6-Ounce Tubes (Pack of 4): 5.00
  Revlon SkinLights Instant Skin Brightener, SPF 15, Warm Light 03, 1.5 Fluid Ounce (44.3 ml): 5.00
  Fantasy by Britney Spears for Women, Set (Eau De Parfum Spray 3.3 Ounce, Body Lotion 3.3 Ounce, Shower Gel 3.3 Ounce): 5.00
  Bvlgari White Eau De Cologne Spray: 5.00
  Cricket Static Free Fast Flo Vent Brush: 5.00
  Qtica Intense Cuticle Repair (select option/size): 5.00
  HAPPY For Men By CLINIQUE Cologne Spray: 5.00
  Corduroy Cologne by Zirh for men Colognes: 5.00
  Chopard Wish Eau de Parfum Spray: 5.00

  Total time for recommending top N: 0.29439425468444824 seconds
  Memory usage: 1113.49609375 MB

  Tuy nhiên nếu chỉ lấy top 10 thì bị trùng max rating là 5 quá nhiều, thử lấy top 50:

  Neutrogena Visibly Firm Body Lotion, Active Copper, 8.5 Ounce (Pack of 2): 5.00
  Oscar By Oscar De La Renta For Women. Eau De Toilette Spray 8 Ounces: 5.00
  So De La Renta By Oscar De La Renta For Women. Eau De Toilette Spray 3.3 Ounces: 5.00
  Basis Cleaner Clean Face Wash, 6-Ounce Tubes (Pack of 4): 5.00
  Revlon SkinLights Instant Skin Brightener, SPF 15, Warm Light 03, 1.5 Fluid Ounce (44.3 ml): 5.00
  OPI Drip Dry Drops Top Nail Coats: 5.00
  Michael Kors: 5.00
  Aw Mendenhall #02303 5lb Heavy Duty Powder Hand Soap: 5.00
  Moisturizing Day Cream: 5.00
  Cricket Static Free Fast Flo Vent Brush: 5.00
  Max Factor Linemaker Waterproof Eyeliner, Rich Black - 1 ea: 5.00
  Neutrogena Neutrogena Fresh Foaming Cleanser: 5.00
  Neutrogena Extra Gentle Cleanser, 6.7 Ounce: 5.00
  Camille Beckman Silky Body Cream: 5.00
  Garnier Nutrisse Haircolor, 452 Dark Reddish Brown Chocolate Cherry: 5.00
  HAPPY For Men By CLINIQUE Cologne Spray: 5.00
  No-Rinse Body Bath with Odor Eliminator - 16 oz.: 5.00
  Perry Ellis Reserve Perfume by Perry Ellis for women Personal Fragrances: 5.00
  Kiss My Face Olive & Lavender Bar Soap, 8-Ounce Bars (Pack of 8): 5.00
  Dark Tanning Xtreme Oil Amplifier: 5.00
  Hawaiian Tropic Aloe After SUN Moisturizer 16 oz. Pump: 5.00
  Canus Li'l Goat's Milk Baby Butter, 8-Ounce Jars (Pack of 3): 5.00
  DUNE For Women By CHRISTIAN DIOR Eau De Toilette Spray: 4.99
  Revlon 1&#34; High&#45;Heat Professional Tourmaline Straightener: 4.99
  Coty Airspun Face Powder 2.3 oz (65 g): 4.99
  Kent OS11 Soft Men's Hairbrush: 4.97
  Victoria's Secret Garden Vanilla Lace 3.4 oz Eau de Toilette Spray: 4.97
  Max Factor Pan-Stik Ultra Creamy Makeup .5 oz (14 g): 4.96
  bareMinerals MATTE SPF 15 Foundation with Click, Lock, Go Sifter: 4.96
  Eau d'Hadrien Perfume by Annick Goutal for women Personal Fragrances: 4.96
  Neutrogena Oil-Free 60-Second Acne Wash Mask Scrub, 6 Ounce: 4.96
  Lumene Premium Beauty Rejuvenating Makeup- 500 Premium Sand (1.0 Fl Oz): 4.96
  Qtica Intense Cuticle Repair (select option/size): 4.95
  Elizabeth Arden Eight Hour Cream Lip Protectant Stick SPF 15 3.7g: 4.95
  Kiehl's Creme De Corps Body Moisturizer: 4.95
  Clayton Shagal Collagen Gel PLUS (Formerly known as Collagen Gel I) - 50 ml / 1.65 oz: 4.94
  Elorac Inc Elorac Inc Packers Pine Tar Soap: 4.94
  New!!Paul Mitchell Tea Tree Special Shampoo One Gallon Size: 4.94
  Liz Claiborne Curve Eau de Toilette Spray: 4.94
  Glysolid Glycerin Cream 1.0 Oz Tube: 4.94
  CIGAR Cologne by Remy Latour for Men - @ Up To 55% Off: 4.93
  Bvlgari Au The'blanc Perfume by Bvlgari for Women. Eau De Cologne Spray 1.3 oz: 4.93
  Chopard Wish Eau de Parfum Spray: 4.93
  CHAMPS ELYSEES For Women By GUERLAIN: 4.93
  Hollywood Beauty Carrot Oil 2 oz.: 4.93
  Marilyn Brush Tuxedo Pro Brush: 4.93
  Mistral Travel Hand Cream in 4 Scents, 1 fl oz: 4.92
  NARCISSE For Women By CHLOE Eau de Toilette Spray: 4.92
  Max Factor Lasting Performance Stay Put Makeup 3 Light Champagne: 4.92
  Zadro Products FG50 Double Vision Suction Cup Mirror: 4.92

- Untuned:
  OPI Drip Dry Drops Top Nail Coats: 4.90
  So De La Renta By Oscar De La Renta For Women. Eau De Toilette Spray 3.3 Ounces: 4.87
  Exuviance Purifying Cleansing Gel-7.2 oz: 4.85
  Styli-Steals Flat Eye Pencils: 4.84
  Liz Claiborne Curve Eau de Toilette Spray: 4.83
  Qtica Intense Cuticle Repair (select option/size): 4.82
  Canus Li'l Goat's Milk Baby Butter, 8-Ounce Jars (Pack of 3): 4.80
  Chopard Wish Eau de Parfum Spray: 4.79
  Corduroy Cologne by Zirh for men Colognes: 4.77
  Bobbi Brown Bronzing Powder: 4.77

  Total time for recommending top N: 0.33663487434387207 seconds
  Memory usage: 1111.68359375 MB
