import numpy as np
import matplotlib.pyplot as plt

time = np.ndarray([])
channel_1 = np.ndarray([])
channel_2 = np.ndarray([])
channel_3 = np.ndarray([])
channel_4 = np.ndarray([])
channel_5 = np.ndarray([])
channel_6 = np.ndarray([])


def array_generation(data):
    global time
    global channel_1
    global channel_2
    global channel_3
    global channel_4
    global channel_5
    global channel_6

    time = np.append(time, data[0])
    channel_1 = np.append(channel_1, data[1])
    channel_2 = np.append(channel_2, data[2])
    channel_3 = np.append(channel_3, data[3])
    channel_4 = np.append(channel_4, data[4])
    channel_5 = np.append(channel_5, data[5])
    channel_6 = np.append(channel_6, data[6])

    return np.vstack((time, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6))


def plot_setup():
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global fig
    global ax1
    global ax2
    global ax3
    global ax4
    global ax5
    global ax6
    plt.ion()
    fig, ax = plt.subplots(figsize=(17, 6))
    ax1 = fig.add_subplot(611)
    ax2 = fig.add_subplot(612)
    ax3 = fig.add_subplot(613)
    ax4 = fig.add_subplot(614)
    ax5 = fig.add_subplot(615)
    ax6 = fig.add_subplot(616)
    ax1.grid()
    ax2.grid()
    ax3.grid()
    ax4.grid()
    ax5.grid()
    ax6.grid()

    t = np.array([])
    ch1 = np.array([])
    ch2 = np.array([])
    ch3 = np.array([])
    ch4 = np.array([])
    ch5 = np.array([])
    ch6 = np.array([])


    line1, = ax1.plot(t, ch1, color = 'red')
    line2, = ax2.plot(t, ch2, color = 'orange')
    line3, = ax3.plot(t, ch3, color = 'blue')
    line4, = ax4.plot(t, ch4, color = 'green')
    line5, = ax5.plot(t, ch5, color = 'pink')
    line6, = ax6.plot(t, ch6, color = 'violet')


def plot_data(time, channel1, channel2, channel3, channel4, channel5, channel6):
    # First create some toy data:
    plt.ion()
    t = time
    ch1 = channel1
    ch2 = channel2
    ch3 = channel3
    ch4 = channel4
    ch5 = channel5
    ch6 = channel6

    t = t[-300:]
    ch1 = ch1[-300:]
    ch2 = ch2[-300:]
    ch3 = ch3[-300:]
    ch4 = ch4[-300:]
    ch5 = ch5[-300:]
    ch6 = ch6[-300:]

    line1.set_xdata(t)
    line1.set_ydata(ch1)
    line2.set_xdata(t)
    line2.set_ydata(ch2)
    line3.set_xdata(t)
    line3.set_ydata(ch3)
    line4.set_xdata(t)
    line4.set_ydata(ch4)
    line5.set_xdata(t)
    line5.set_ydata(ch5)
    line6.set_xdata(t)
    line6.set_ydata(ch6)
    ax1.set(xlim=(min(t), max(t)), ylim=(min(ch1), max(ch1)))
    ax2.set(xlim=(min(t), max(t)), ylim=(min(ch2), max(ch2)))
    ax3.set(xlim=(min(t), max(t)), ylim=(min(ch3), max(ch3)))
    ax4.set(xlim=(min(t), max(t)), ylim=(min(ch4), max(ch4)))
    ax5.set(xlim=(min(t), max(t)), ylim=(min(ch5), max(ch5)))
    ax6.set(xlim=(min(t), max(t)), ylim=(min(ch6), max(ch6)))
    plt.tight_layout()
    fig.canvas.flush_events()


