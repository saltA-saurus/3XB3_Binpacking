import matplotlib.pyplot as plt
import json

class GetData:
        
        def load_json_data(filename): # filename = 'out/plot_data.json'
                file = open(filename)
                plot_data = json.load(file)
                file.close()
                return plot_data
        
        def extract_json_data(plot_data, kpi):
                algorithms = list(plot_data.keys())
                datasets = list(plot_data[algorithms[0]].keys())

                online_data = [[] for i in range(len(datasets))]
                offline_data = [[] for i in range(len(datasets))]

                # algorithms: NextFitOnline, FirstFitOnline, BestFitOnline, WorstFitOnline, NextFitOffline, FirstFitOffline, BestFitOffline, WorstFitOffline
                # datasets: N4C2W2_A.BPP.txt N4C2W2_B.BPP.txt
                for i in range(len(algorithms)): # 0 - 7
                        isOnline = True
                        if 'Offline' in algorithms[i]:
                                isOnline = False
                        for j in range(len(datasets)): # A - T
                                if isOnline:
                                        online_data[j].append(float(plot_data[algorithms[i]][datasets[j]][kpi]))
                                elif not isOnline:
                                        offline_data[j].append(float(plot_data[algorithms[i]][datasets[j]][kpi]))

                return (online_data, offline_data, algorithms, datasets)
        
        def average_data(plot_data):

                online_data = plot_data[0]
                offline_data = plot_data[1]
                algorithms = plot_data[2]
                datasets = plot_data[3]

                average_online_data = [0 for i in range(len(online_data[0]))]
                average_offline_data = [0 for i in range(len(offline_data[0]))]


                for i in range(len(datasets)):
                        for j in range(len(online_data[0])):
                                average_online_data[j] += online_data[i][j]
                        for j in range(len(offline_data[0])):
                                average_offline_data[j] += offline_data[i][j]

                for i in range(len(average_online_data)):
                        average_online_data[i] /= len(datasets)
                for i in range(len(average_offline_data)):
                        average_offline_data[i] /= len(datasets)
                
                avg_plot_data = (average_online_data, average_offline_data, algorithms, datasets)

                return avg_plot_data
        

class PlotGraph:

        def plot_benchmark(plot_data, title, y_axis_label, x_axis_label):
                
                online_data = plot_data[0]
                offline_data = plot_data[1]
                algorithms = plot_data[2]
                datasets = plot_data[3]
                
                n1 = len(online_data)
                n2 = len(offline_data)
                r1 = [] 
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

                while len(online_data) != len(offline_data):
                        if len(online_data) > len(offline_data):
                                offline_data.append(0)
                        else:
                                online_data.append(0)

                # debug
                # print('Algorithms:', algorithms)
                # print('Datasets:', datasets)
                # print('Online Data:', online_data)
                # print('Offline Data:', offline_data)

                plt.bar(r1, online_data, color='orangered',
                        width=width, edgecolor='black',
                        label='Online')
                plt.bar(r2, offline_data, color = 'deepskyblue',
                        width=width, edgecolor = 'black',
                        label='Offline')
                
                plt.xlabel(x_axis_label)
                plt.ylabel(y_axis_label)
                plt.title(title)
                
                plt.xticks(r3, x_tick_strings)
                plt.legend()
                
                plt.show()
