# # coding=utf8
# import psutil
# import time
# from threading import Lock
# from app.main import socketio
#
# # Set this variable to "threading", "eventlet" or "gevent" to test the
# # different async modes, or leave it set to None for the application to choose
# # the best option based on installed packages.
# thread = None
# thread_lock = Lock()
#
#
# # 后台线程 产生数据，即刻推送至前端
# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         socketio.sleep(5)
#         count += 1
#         # 获取系统时间（只取分:秒）
#         t = time.strftime('%M:%S', time.localtime())
#         # 获取系统cpu使用率 non-blocking
#         cpus = psutil.cpu_percent(interval=None, percpu=True)
#         # 注意：这里不需要客户端连接的上下文，默认 broadcast = True ！！！！！！！
#         socketio.emit('server_response', {'data': [t, *cpus], 'count': count}, namespace='/test')
#
#
# # 与前端建立 socket 连接后，启动后台线程
# @socketio.on('connect', namespace='/test')
# def test_connect():
#     global thread
#     with thread_lock:
#         if thread is None:
#             thread = socketio.start_background_task(target=background_thread)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # total_mem = psutil.virtual_memory().total
# # # print("your total menmory is")
# # # print(total_mem / 1024 / 1024 / 1024)
# #
# #
# # def getProcessInfo(p):
# #     """取出指定进程占用的进程名，进程ID，进程实际内存使用率, 虚拟内存使用率,CPU使用率"""
# #     try:
# #         cpu = p.cpu_percent(interval=0)
# #         rss, vms = p.memory_info().rss, p.memory_info().vms
# #         name = p.name()
# #         pid = p.pid
# #         cpio = p.io_counters()
# #         return [name, pid, rss * 100 / total_mem, vms * 100 / total_mem, cpu, cpio]
# #     except Exception as e:
# #         pass
# #     finally:
# #         pass
# #
# #
# # def getAllProcessInfo():
# #     """取出全部进程的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率"""
# #     t = round(time.time())
# #     # us = str(psutil.users()[0].name)
# #     instances = []  # ['name, pid, 进程实际内存, 虚拟内存,CPU使用率']
# #     all_processes = list(psutil.process_iter())
# #     for proc in all_processes:
# #         try:
# #             proc.cpu_percent(interval=0)
# #         except Exception as e:
# #             pass
# #         else:
# #             pass
# #         finally:
# #             pass
# #
# #     # 此处sleep1秒是取正确取出CPU使用率的重点
# #     time.sleep(1)
# #     for proc in all_processes:
# #         instances.append(getProcessInfo(proc))
# #     return instances
# #
# # # 获取进程信息，通过http请求传入服务器
# # def postData():
# #     res = getAllProcessInfo()
# #     dict = {}
# #     name = []
# #     pid = []
# #     rss = []
# #     vms = []
# #     cpu = []
# #     rold = 0
# #     vold = 0
# #     for d1 in res:
# #         if d1 is not None :
# #             # name, pid, rss * 100 / total_mem, vms * 100 / total_mem, cpu, cpio
# #             name.append(d1[0])
# #             pid.append(d1[1])
# #             rss.append(d1[2])
# #             vms.append(d1[3])
# #             cpu.append(d1[4])
# #             rold += d1[2]
# #             vold += d1[3]
# #     name.append("总共")
# #     pid.append(-1)
# #     rss.append(100-rold)
# #     vms.append(100-vold)
# #     cpu.append(-1)
# #     dict["name"] = name
# #     dict["pid"] = pid
# #     dict["rss"] = rss
# #     dict["vms"] = vms
# #     dict["cpu"] = cpu
# #     return dict
# #
# #
# # def postData1():  # 获取进程信息，通过http请求传入服务器
# #     res = getAllProcessInfo()
# #     return res
# #
# # def postData2():  # 获取进程信息，通过http请求传入服务器
# #     res = getAllProcessInfo()
# #     dict = {}
# #     name = []
# #     pid = []
# #     rss = []
# #     vms = []
# #     cpu = []
# #     for d1 in res:
# #         if d1 is not None and d1[1] != 0:
# #             # name, pid, rss * 100 / total_mem, vms * 100 / total_mem, cpu,cpio
# #             name.append(d1[0])
# #             pid.append(d1[1])
# #             rss.append(d1[2])
# #             vms.append(d1[3])
# #             cpu.append(d1[4])
# #     dict["name"] = name
# #     dict["pid"] = pid
# #     dict["rss"] = rss
# #     dict["vms"] = vms
# #     dict["cpu"] = cpu
# #     return dict
#
#
#
