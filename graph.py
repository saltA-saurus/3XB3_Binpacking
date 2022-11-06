import matplotlib.pyplot as plt
import json

class GetJsonData:
        
        def load_json_data(filename): # filename = 'out/plot_data.json'
                file = open(filename)
                plot_data = json.load(file)
                file.close()
                return plot_data
        

class PlotBenchmark:

        def plot_benchmark(plot_data, title, y_axis_label, x_axis_label, kpi, dataset_name):
                
                algorithms = list(plot_data.keys())
                datasets = list(plot_data[algorithms[0]].keys())
                datasetInd = datasets.index(dataset_name)

                online_data = [[] for i in range(len(datasets))]
                offline_data = [[] for i in range(len(datasets))]
                
                # algorithms: NextFitOnline, FirstFitOnline, BestFitOnline, WorstFitOnline, NextFitOffline, FirstFitOffline, BestFitOffline, WorstFitOffline
                # datasets: N4C2W2_A.BPP.txt N4C2W2_B.BPP.txt
                for i in range(len(algorithms)): # 0 - 7
                        isOnline = True
                        if 'Offline' in algorithms[i]:
                                isOnline = False
                        for j in range(len(datasets)): # 0 - 1
                                if isOnline:
                                        online_data[j].append(float(plot_data[algorithms[i]][datasets[j]][kpi]))
                                elif not isOnline:
                                        offline_data[j].append(float(plot_data[algorithms[i]][datasets[j]][kpi]))
                
                n1 = len(online_data[0])
                n2 = len(offline_data[0])
                r1 = [] # num of online algos
                for i in range(max(n1, n2)):
                        r1.append(i)
                width = 0.25
                r2 = [n + width for n in r1]
                r3 = [n + width/2 for n in r1]

                x_tick_strings = []
                for algo in algorithms:
                        if 'Online' in algo:
                                if algo.replace('Online', '') not in x_tick_strings:
                                        x_tick_strings.append(algo.replace('Online', ''))
                        if 'Offline' in algo:
                                if algo.replace('Offline', '') not in x_tick_strings:
                                        x_tick_strings.append(algo.replace('Offline', ''))

                # debug
                print('Algorithms:', algorithms)
                print('Datasets:', datasets)
                print('Online Data:', online_data)
                print('Offline Data:', offline_data)

                plt.bar(r1, online_data[datasetInd], color='r', width=width, edgecolor='black', label='Online')
                plt.bar(r2, offline_data[datasetInd], color = 'b',
                        width=width, edgecolor = 'black',
                        label='Offline')
                
                plt.xlabel(x_axis_label)
                plt.ylabel(y_axis_label)
                plt.title(title)
                
                plt.xticks(r3, x_tick_strings)
                plt.legend()
                
                plt.show()

# test runner DELETE LATER
def main():
        plot_data = GetJsonData.load_json_data('out/plot_data.json')
        PlotBenchmark.plot_benchmark(plot_data, 'title', 'hello', 'bye', 'Bins Used', 'N4C2W2_A.BPP.txt')
main()

             