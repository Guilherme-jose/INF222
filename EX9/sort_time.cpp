#include <iostream>
#include <algorithm>
#include <vector>
#include <chrono>

void custom_sort(std::vector<float>& arr, int low, int high) { // algoritmo quicksort gerado pelo copilot
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        custom_sort(arr, low, i);
        custom_sort(arr, i + 2, high);
    }
}

int main() {
    std::vector<float> arr(1000000);
    std::generate(arr.begin(), arr.end(), []() { return static_cast<float>(std::rand()) / (static_cast<float>(RAND_MAX / 1000.0)); });

    auto start = std::chrono::high_resolution_clock::now();

    std::sort(arr.begin(), arr.end());

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    std::cout << "Time taken to sort: " << elapsed.count() << " seconds" << std::endl;

    std::generate(arr.begin(), arr.end(), []() { return static_cast<float>(std::rand()) / (static_cast<float>(RAND_MAX / 1000.0)); });

    start = std::chrono::high_resolution_clock::now();

    custom_sort(arr, 0, arr.size() - 1);

    end = std::chrono::high_resolution_clock::now();
    elapsed = end - start;

    std::cout << "Time taken to custom sort: " << elapsed.count() << " seconds" << std::endl;

    arr.resize(2000000);
    std::generate(arr.begin(), arr.end(), []() { return static_cast<float>(std::rand()) / (static_cast<float>(RAND_MAX / 1000.0)); });

    start = std::chrono::high_resolution_clock::now();

    std::sort(arr.begin(), arr.end());

    end = std::chrono::high_resolution_clock::now();
    elapsed = end - start;

    std::cout << "Time taken to sort 2 million elements: " << elapsed.count() << " seconds" << std::endl;

    std::generate(arr.begin(), arr.end(), []() { return static_cast<float>(std::rand()) / (static_cast<float>(RAND_MAX / 1000.0)); });

    start = std::chrono::high_resolution_clock::now();

    custom_sort(arr, 0, arr.size() - 1);

    end = std::chrono::high_resolution_clock::now();
    elapsed = end - start;

    std::cout << "Time taken to custom sort 2 million elements: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}


