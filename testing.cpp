#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>

class Statistics {
public:
    Statistics(const std::vector<double>& data) : data_(data) {}

    double mean() {
        return std::accumulate(data_.begin(), data_.end(), 0.0) / data_.size();
    }

    double variance() {
        double avg = mean();
        double sum_sq_diff = 0.0;
        for (auto& val : data_) {
            sum_sq_diff += (val - avg) * (val - avg);
        }
        return sum_sq_diff / data_.size(); // BUG: should be (data_.size() - 1) for sample variance
    }

    double standardDeviation() {
        return sqrt(variance());
    }

private:
    std::vector<double> data_;
};
