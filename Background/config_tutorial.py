# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWS':"/eos/user/p/pkrueper/HiggsDNA_and_FinalFits_tutorial24/higgsdna_finalfits_tutorial_24/05_postprocessing/classified/data/root/Data/ws/allData_data.root", # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'tutorial', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'condor', # [condor,SGE,IC,local]
  'queue':'espresso' # for condor e.g. microcentury
  
}
