Source for Collaborative Filtering method

Kết quả thử nghiệm 100 record rating:

| Algorithm | RMSE   | MAE    | HR     | cHR    | ARHR   | Coverage | Diversity | Novelty |
| --------- | ------ | ------ | ------ | ------ | ------ | -------- | --------- | ------- |
| User KNN  | 1.6429 | 1.2560 | 0.0000 | 0.0000 | 0.0000 | 1.0000   | 0.9789    | 9.9732  |
| Item KNN  | 1.6316 | 1.2016 | 0.0366 | 0.0366 | 0.0366 | 1.0000   | 0.9789    | 9.9732  |
| Random    | 2.0021 | 1.3880 | 0.0366 | 0.0366 | 0.0305 | 1.0000   | 0.9352    | 11.8903 |

Kết quả thử nghiệm 10k record rating:

Number of users in the trainset: 9238
Number of items in the trainset: 1346

| Algorithm | RMSE   | MAE    | HR     | cHR    | ARHR   | Coverage | Diversity | Novelty  |
| --------- | ------ | ------ | ------ | ------ | ------ | -------- | --------- | -------- |
| User KNN  | 1.3079 | 1.0350 | 0.0011 | 0.0011 | 0.0005 | 1.0000   | 0.9778    | 516.2702 |
| Item KNN  | 1.2922 | 1.0048 | 0.0049 | 0.0049 | 0.0047 | 1.0000   | 0.9784    | 515.8840 |
| Random    | 1.6667 | 1.2511 | 0.0009 | 0.0009 | 0.0005 | 1.0000   | 0.9783    | 581.0095 |

Max RAM consume: 6GB
