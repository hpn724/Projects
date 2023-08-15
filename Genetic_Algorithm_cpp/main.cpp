#include <iostream>
#include <iterator>
#include <math.h>
#include <random>
#include <vector> 
#include <algorithm>

const int sample_size=1000; // How many top solutions to select
const int num_of_solutions=100000;       // Number of solutions per generation

struct Solution
{   
    double rank, x,y,z;
    void fitness()
    {
        double ans = (6 * x + -y + std::pow(z,200)) - 25;
        rank = (ans == 0) ? 9999 : std::abs(1/ans);

    }
};

int main()
{
    //create initial solutions
    std::random_device rand_dev;
    std::uniform_real_distribution<double> unif_dist(-100,100);
    std::vector<Solution> solutions;

    
    for(int i=0;i<num_of_solutions;i++)
    {
        solutions.push_back(Solution{0,unif_dist(rand_dev),unif_dist(rand_dev),unif_dist(rand_dev)});
    }

    //Run the fitness function

    while(true)
    {    
        for(auto& s : solutions) 
        {
            s.fitness();
        }

        //sort our solutions by rank

        std::sort(solutions.begin(),solutions.end(),
        [](const auto& lhs, const auto& rhs){
                return lhs.rank>rhs.rank;
        });

        std::for_each(
            solutions.begin(),
            solutions.begin()+10,
            [](const auto& s)
            {
                std::cout<<std::fixed
                << " Rank "<< static_cast<int>(s.rank)
                <<"\n x:"<<s.x<<"\t y:"<<s.y<<"\t z:"<<s.z<<"\n";
            }
        );

        //take the top solutions 
        ;
        std::vector<Solution> sample;
        std::copy(solutions.begin(),solutions.begin()+sample_size,std::back_inserter(sample));
        solutions.clear();

        //Mutate the solutions by %

        std::uniform_real_distribution<double> m(0.99,1.01);
        std::for_each(sample.begin(),sample.end(),[&](auto& s){
            s.x *=m(rand_dev);
            s.y *=m(rand_dev);
            s.z *=m(rand_dev);
        });

        //Cross over

        std::uniform_int_distribution<int> cross(0,sample_size-1);
        for(int i=0;i<num_of_solutions;i++)
        {
            solutions.push_back(Solution{0,sample[cross(rand_dev)].x,sample[cross(rand_dev)].y,sample[cross(rand_dev)].z});
        }
    }
}