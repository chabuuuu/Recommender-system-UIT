Source for Collaborative Filtering method

Kết quả thử nghiệm 100 record rating:

| Algorithm | RMSE   | MAE    | HR     | cHR    | ARHR   | Coverage | Diversity | Novelty |
| --------- | ------ | ------ | ------ | ------ | ------ | -------- | --------- | ------- |
| User KNN  | 1.6429 | 1.2560 | 0.0000 | 0.0000 | 0.0000 | 1.0000   | 0.9789    | 9.9732  |
| Item KNN  | 1.6316 | 1.2016 | 0.0366 | 0.0366 | 0.0366 | 1.0000   | 0.9789    | 9.9732  |
| Random    | 2.0021 | 1.3880 | 0.0366 | 0.0366 | 0.0305 | 1.0000   | 0.9352    | 11.8903 |

Top 10 result:

- User KNN:
  Oscar Eau de Toilette for Women by Oscar de La Renta: 4.21
  Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 4.21
  Michel Design Works Bath Gift Set - Beach: 4.21
  Liz Claiborne Curve Eau de Toilette Spray: 4.21
  Palladio Herbal Lipstick,: 4.21
  SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.21
  Island Essence Lotion: 4.21
  Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.21
  Island Essence Lotion: 4.21
  Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.21

  Total time for recommending top N: 0.0009508132934570312 seconds
  Memory usage: 69.6796875 MB

- Item KNN:
  Oscar Eau de Toilette for Women by Oscar de La Renta: 4.21
  Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 4.21
  Michel Design Works Bath Gift Set - Beach: 4.21
  Liz Claiborne Curve Eau de Toilette Spray: 4.21
  Palladio Herbal Lipstick,: 4.21
  SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.21
  Island Essence Lotion: 4.21
  Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.21
  Island Essence Lotion: 4.21
  Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.21

  Total time for recommending top N: 0.0007684230804443359 seconds
  Memory usage: 68.01171875 MB

Kết quả thử nghiệm 10k record rating:

Number of users in the trainset: 9238
Number of items in the trainset: 1346

| Algorithm | RMSE   | MAE    | HR     | cHR    | ARHR   | Coverage | Diversity | Novelty  |
| --------- | ------ | ------ | ------ | ------ | ------ | -------- | --------- | -------- |
| User KNN  | 1.3079 | 1.0350 | 0.0011 | 0.0011 | 0.0005 | 1.0000   | 0.9778    | 516.2702 |
| Item KNN  | 1.2922 | 1.0048 | 0.0049 | 0.0049 | 0.0047 | 1.0000   | 0.9784    | 515.8840 |

Top 10 result:

- User KNN:
  Oscar Eau de Toilette for Women by Oscar de La Renta: 4.17
  Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 4.17
  Michel Design Works Bath Gift Set - Beach: 4.17
  Liz Claiborne Curve Eau de Toilette Spray: 4.17
  Palladio Herbal Lipstick,: 4.17
  SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.17
  Island Essence Lotion: 4.17
  Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.17
  Island Essence Lotion: 4.17
  Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.17

  Total time for recommending top N: 1.2743637561798096 seconds
  Memory usage: 1720.73828125 MB

- Item KNN:
  Oscar Eau de Toilette for Women by Oscar de La Renta: 4.17
  Optimum Care Anti-Breakage Therapy Moisture Replenish Cream Hairdress: 4.17
  Michel Design Works Bath Gift Set - Beach: 4.17
  Liz Claiborne Curve Eau de Toilette Spray: 4.17
  Palladio Herbal Lipstick,: 4.17
  SOFT SHEEN Carson Optimum Care Anti-Breakage Therapy Featherlight Hairdress 4oz/113g: 4.17
  Island Essence Lotion: 4.17
  Creed Spring Flower by Creed for Women - 2.5 oz Millesime Spray: 4.17
  Island Essence Lotion: 4.17
  Azulen Supreme Facial Cream 1.66 oz by Dr. Eckstein: 4.17

  Total time for recommending top N: 0.03168225288391113 seconds
  Memory usage: 1179.25 MB
