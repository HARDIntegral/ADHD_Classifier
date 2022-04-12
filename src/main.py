from data_manager.data_grabber import  bucket_data
from data_manager.data_manipulation import RestrictType, data_avg, avg_slope, avg_value

from run_models import run

def main():
    # load the data
    adhd, ctrl = bucket_data('data_location.json')

    # assign features to the data
    for e, d in zip(adhd, list(zip(avg_slope(adhd, restrict = RestrictType.NORM), avg_value(adhd, restrict = RestrictType.NORM)))):
        e.add_features(d[0] + d[1])
    for e, d in zip(ctrl, list(zip(avg_slope(ctrl, restrict = RestrictType.NORM), avg_value(ctrl, restrict = RestrictType.NORM)))):
        e.add_features(d[0] + d[1]) 

    run (adhd, ctrl)

if __name__ == '__main__':
    main()