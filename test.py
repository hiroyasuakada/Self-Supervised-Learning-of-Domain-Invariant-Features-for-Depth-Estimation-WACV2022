import os
from options.test_options import TestOptions
from dataloader.data_loader import dataloader
from model.models import create_model
from util.visualizer import Visualizer
from util import html

opt = TestOptions().parse()
opt.dataset_mode = 'paired'

dataset = dataloader(opt)
dataset_size = len(dataset) * opt.batch_size
print ('testing images = %d ' % dataset_size)

model = create_model(opt)
visualizer = Visualizer(opt)

web_dir = os.path.join(opt.results_dir,opt.experiment_name, '%s_%s' %(opt.phase, opt.which_epoch))
web_page = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.experiment_name, opt.phase, opt.which_epoch))

# testing
for i,data in enumerate(dataset):
    model.set_input(data)
    model.test()
    model.save_results(visualizer, web_page)

    if i == opt.ntest:
        break