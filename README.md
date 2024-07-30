

# e2calib-xjh
在对多模系统进行标定的时候，首先需要对采集到的事件进行重建，我们使用e2calib来根据时间戳进行重建，原代码可以在[这里](https://github.com/uzh-rpg/e2calib)找到，为了方便处理，建议跟着本项目的步骤进行。
  
## 环境

* 建议使用python3.8
	```
	conda create --name XJHNet python=3.8.18
	```
* 参考的torch版本
	```bash
	conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
	```
* 其他相关库安装
	```
	pip install -r requirements.txt
	```
## 运行步骤
* ### STEP 1

	首先需要将事件相机采集到的raw文件转换成h5文件
	```bash
	python .\python\convert.py PATH_TO_YOUR_RAW_FILE -o .\h5data\event.h5
	```
	运行上面程序的时候，注意把`PATH_TO_YOUR_RAW_FILE`修改为raw文件的地址，比如说你可以运行下列命令：

	**示例**：
	```bash
	python .\python\convert.py F:\Data\000001\event.raw -o .\h5data\event.h5
	```
	**Tips**：考虑到可能会多次使用该工程，我加了个判断，如果h5文件的位置已经被占用了，会直接覆盖上次的h5文件。所以如果你不是很在意空间的话，不用每次都手动删掉生成的h5文件。


* ### STEP 2
	需要注意的是，多模系统生成的时间戳和e2calib的时间戳是不一样的，因此一定要用下面的代码转换一下格式。
	```bash
	python timestamp_convert.py -i PATH_TO_YOUR_TIMESTAMP_FILE
	```
	其中`PATH_TO_YOUR_TIMESTAMP_FILE`为时间戳的地址，比如说你可以运行：

	**示例**：
	```bash
	python timestamp_convert.py -i F:\Data\000001\timestamp.txt
	```

	**Tips**：和h5文件一样，生成的时间戳会自动覆盖上次的记录。

* ### STEP 3
	接下来运行下面的代码开始重建，你需要的结果会存放在指定路径下（`NAME_YOU_WANT`）
	```bash
	python python\offline_reconstruction.py --dataset_name NAME_YOU_WANT --upsample_rate 2 --h5file .\h5data\event.h5 --output_folder .\output --timestamps_file timestamp_convert.txt --height 720 --width 1280 --use_gpu
	```

* ### STEP 4
	最后，由于分光镜将事件模态进行了左右翻转，我们需要用`reverse_rename.py`将重建结果翻回来并重命名。

	**Tips**：
	1、代码中的 input_foler 和 output_folder 分别指重建图文件夹路径和处理后的路径，需要直接在代码上修改。
	2、如果你用的是低光双模三相机系统，那就不需要将事件左右翻转，而应该翻转帧图像，在那个项目的步骤中有具体操作，跳过本文档的STEP4即可。

## WARNING !
有必要提醒一下，以上步骤是针对我们实验室多模态系统采集软件设计的。
如果你想要使用已有的h5文件，可以参考`h52h5.py` 文件。
如果你的事件相机分辨率不是1280*720，需要调整STEP3中的代码。
