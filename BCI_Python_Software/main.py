import UDP_connect as Udp
import Plots
# import GUI_Open_BCI

if __name__ == '__main__':
    
    Plots.plot_setup()
    while 1:
        #app = GUI_Open_BCI.GUI
        ESP_Data = Udp.collect_data()
        Array_Data = Plots.array_generation(ESP_Data)
        Plots.plot_data(Array_Data[0], Array_Data[1], Array_Data[2], Array_Data[3], Array_Data[4], Array_Data[5],
                        Array_Data[6])
