#include <iostream>
#include <cstdint>
#include <vector>
#include <iomanip>
#include <string>

inline uint32_t reduce_mod9(uint64_t value) {
    return value % 9;
}

struct NodeState {
    uint64_t tick;
    uint32_t pace;
    uint64_t raw_step;
    uint32_t node_index;
    uint32_t angle_deg;
    uint32_t digital_root;
};

class HarmonicEngine {
private:
    static constexpr uint32_t STEP_MULTIPLIER = 13;
    static constexpr uint32_t GRID_SIZE = 144;
    static constexpr uint32_t ANGLE_BASE = 36;

public:
    NodeState calculate_step(uint64_t tick, uint32_t pace) const {
        uint64_t raw_step = tick * STEP_MULTIPLIER * pace;
        uint32_t node = raw_step % GRID_SIZE;
        uint32_t angle = (raw_step * ANGLE_BASE) % 360;
        uint32_t root = reduce_mod9(raw_step);

        return {tick, pace, raw_step, node, angle, root};
    }

    void run_simulation(uint64_t max_ticks) const {
        const uint32_t paces[3] = {1, 2, 3};

        std::cout << std::left 
                  << std::setw(8)  << "Tick"
                  << std::setw(8)  << "Pace"
                  << std::setw(14) << "Raw Stride"
                  << std::setw(12) << "Node (144)"
                  << std::setw(10) << "Angle"
                  << std::setw(8)  << "Mod-9" << "\n";
        std::cout << std::string(60, '-') << "\n";

        for (uint64_t tick = 1; tick <= max_ticks; ++tick) {
            for (uint32_t pace : paces) {
                NodeState state = calculate_step(tick, pace);
                std::cout << std::left 
                          << std::setw(8)  << state.tick
                          << std::setw(8)  << state.pace
                          << std::setw(14) << state.raw_step
                          << std::setw(12) << state.node_index
                          << std::setw(10) << (std::to_string(state.angle_deg) + "°")
                          << std::setw(8)  << state.digital_root << "\n";
            }
        }
    }
};

int main() {
    HarmonicEngine engine;
    engine.run_simulation(10);
    return 0;
}
