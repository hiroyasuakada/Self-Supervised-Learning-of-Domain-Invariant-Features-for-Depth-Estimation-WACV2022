set -ex
python test.py \
    --model test \
    --img_source_dir ../datasets/vkitti_data/train_color \
    --img_target_dir ./datasplit/eigen_test_files.txt \
    --lab_source_dir ../datasets/vkitti_data/train_depth \
    --lab_target_dir ./datasplit/eigen_test_files.txt \
    --txt_data_path ../datasets/kitti_data/ \
    --load_size 960 288 \
    --gpu_ids 1 --ntest 697 --norm batch --pre_trained_on_ImageNet \
    --batch_size 1 \
    --experiment_name vkitti2kitti_full-fine \
    --which_epoch best
