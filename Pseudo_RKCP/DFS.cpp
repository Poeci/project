#include <iostream>
#include <vector>

const int amount_of_connections = 93788, amount_of_words = 24661, how_long = 40;

void input(std::vector<std::vector<std::pair<int, int>>> &graph, std::vector<std::string> &words)
{
	for(int i = 0, from, to, type; i < amount_of_connections; i++)
	{
		std::cin >> from >> to >> type;

		graph[from].push_back({to, type});
	}
	std::string junk;
	std:: cin >> junk;
	for(int i = 0, tmp; i < amount_of_words; i++)
	{
		std::cin >> tmp >> words[i];
	} 
}

bool dfs(int current, int size, std::vector<std::vector<std::pair<int, int>>> &graph, std::vector<int> &result_words, std::vector<int> &result_signs, std::vector<int> &visited_by)
{
	if(size == how_long)
	{
		result_words[size-1] = current;
		return true;
	}
	for(int i = 0, tmp; i < 2*graph[current].size(); i++)
	{
		tmp = rand() % (graph[current].size());
		if(visited_by[graph[current][tmp].first] != current)
		{
			visited_by[graph[current][tmp].first] = current;
			if(dfs((graph[current][tmp].first), size+1, graph, result_words, result_signs, visited_by))	
			{
				result_words[size-1] = current;
				result_signs[size-1] = graph[current][tmp].second;
				return true;
			}
		}

	}
	return false;
}

bool generate(int current, std::vector<std::vector<std::pair<int, int>>> &graph, std::vector<std::string> &words)
{
	std::vector<int> result_words(how_long);
	std::vector<int> result_signs(how_long);
	std::vector<int> visited_by(amount_of_words);
	result_words[how_long-1] = -1;
	dfs(current, 1, graph, result_words, result_signs, visited_by);
	
	if(result_words[how_long-1] == -1)
		return false;

	for(int i = 0; i < how_long; i++)
	{
		std::cout << words[result_words[i]];
		switch(result_signs[i])
		{
			case 0 : std::cout << " ";
				break;
			case 1 : std::cout << ", ";
				break;
			case 2 : std::cout << ". ";
				break;
			case 3 : std::cout << std::endl;
				break;
			case 4 : std::cout << "... ";
				break;
			case 5 : std::cout << "? ";
				break;
			case 6 : std::cout << "! ";
				break;
			case 7 : std::cout << " - ";
				break;
			case 8 : std::cout << ": ";
				break;		
			case 9 : std::cout << "; ";
				break;
		}							
	}
	std::cout << std::endl;
	return true;
}

int main()
{
	srand (time(NULL));

	std::vector<std::vector<std::pair<int, int>>> graph(amount_of_words);
	std::vector<std::string> words(amount_of_words);
	input(graph, words);
	for(int i = 0; i < amount_of_words; i++)
	{
		int tmp = rand() % (amount_of_words);
		if(generate(tmp, graph, words))
			break;
	}
	return 0;
}