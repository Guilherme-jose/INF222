#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

std::vector<double> generate_random_list(int size, bool uniform) {
    std::vector<double> random_list;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-1000, 1000);

    if (uniform) {
        int num_zeroes = size / 20;
        int num_non_zeroes = size - num_zeroes;
        for (int i = 0; i < num_non_zeroes; ++i) {
            random_list.push_back(dis(gen));
        }
        for (int i = 0; i < num_zeroes; ++i) {
            random_list.push_back(0);
        }
    } else {
        int num_negatives = size / 3;
        int num_positives = size / 3;
        int num_zeroes = size - num_negatives - num_positives;
        std::uniform_real_distribution<> neg_dis(-1000, -1);
        std::uniform_real_distribution<> pos_dis(1, 1000);

        for (int i = 0; i < num_negatives; ++i) {
            random_list.push_back(neg_dis(gen));
        }
        for (int i = 0; i < num_positives; ++i) {
            random_list.push_back(pos_dis(gen));
        }
        for (int i = 0; i < num_zeroes; ++i) {
            random_list.push_back(0);
        }
    }

    std::shuffle(random_list.begin(), random_list.end(), gen);
    return random_list;
}

void dutch_flag_partition(std::vector<double>& arr) {
    int low = 0, mid = 0, high = arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] < 0) {
            std::swap(arr[low++], arr[mid++]);
        } else if (arr[mid] > 0) {
            std::swap(arr[mid], arr[high--]);
        } else {
            ++mid;
        }
    }
}

void test(std::vector<int> setting) {
    int size = (setting[1] == -1) ? 1000000 : 2000000;
    bool uniform = (setting[3] == 1);
    std::vector<double> random_list = generate_random_list(size, uniform);

    if (setting[2] == 1) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, random_list.size() - 1001);
        for (int i = 0; i < 1000; ++i) {
            int start = dis(gen);
            int end = start + 1000;
            std::sort(random_list.begin() + start, random_list.begin() + end);
        }
    }

    auto start_time = std::chrono::high_resolution_clock::now();

    if (setting[0] == -1) {
        std::sort(random_list.begin(), random_list.end());
    } else {
        dutch_flag_partition(random_list);
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    std::cout << "Setting: [" << setting[0] << ", " << setting[1] << ", " << setting[2] << ", " << setting[3] << "]\n";
    std::cout << "Execution time: " << elapsed.count() << " seconds\n";
}

void test_all_combinations() {
    //for (int uniform : {-1, 1}) {
        for (int ordered : {-1, 1}) {
            for (int size : {-1, 1}) {
                for (int algorithm : {-1, 1}) {
                    std::vector<int> setting = {algorithm, size, ordered, 1};
                    test(setting);
                }
            }
        }
    //}
}

int main() {
    for (int i = 0; i < 5; ++i) {
        //test_all_combinations();
        //std::cout << "done\n";
    }
    
    
    std::cout << "2^5-2\n";
    std::vector<std::vector<int>> t = {
        {-1, -1, -1, -1},
        { 1, -1, -1,  1},
        {-1,  1,  1, -1},
        { 1,  1,  1,  1},
    };

    for (const auto& setting : t) {
        test(setting);
    }
    
   return 0;
}