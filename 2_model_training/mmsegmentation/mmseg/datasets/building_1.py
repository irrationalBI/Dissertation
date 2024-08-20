from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class BuildingDataset(BaseSegDataset):
    # Category and corresponding RGB color scheme
    METAINFO = {
        'classes':['background', 'building'],
        'palette':[[0,0,0], [255,255,255]]
    }
    
    # Specify image extension and annotation extension
    def __init__(self,
                 seg_map_suffix='.png',   # Format of annotated mask images
                 reduce_zero_label=False, # The category with category ID 0 be removed or not
                 **kwargs) -> None:
        super().__init__(
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)