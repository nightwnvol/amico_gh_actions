from os.path import join as pjoin
import pathlib
import amico

# version
ver = amico.__version__
# verbose
amico.set_verbose(2)
# kernels
regenerate = True
print('\033[92m' + f'Running AMICO v{amico.__version__}' + '\033[0m')
sub = 'demo'
bval = 'NODDI_protocol.bval'
bvec = 'NODDI_protocol.bvec'
scheme = 'scheme.txt'
b_step = 1
dwi = 'NODDI_DWI.img'
mask = 'brain_mask.img'
b0_thr = 0
ndirs = 500
# paths
study_path = pjoin(pathlib.Path(__file__).parent.resolve())
out_path = pjoin(pathlib.Path(__file__).parent.resolve(), 'res_' + ver, sub)
amico.setup()
amico.util.fsl2scheme(bvalsFilename=pjoin(study_path, sub, bval), bvecsFilename=pjoin(study_path, sub, bvec), schemeFilename=pjoin(study_path, sub, scheme), bStep=b_step)
ae = amico.Evaluation(study_path=study_path, subject=sub, output_path=out_path)
ae.set_config('doComputeRMSE', True)
ae.set_config('doComputeNRMSE', True)
ae.set_config('doSaveodulatedMaps', True)
ae.load_data(dwi_filename=dwi, scheme_filename=scheme, mask_filename=mask, b0_thr=b0_thr)
ae.set_model('NODDI')
ae.generate_kernels(regenerate=regenerate, ndirs=ndirs)
ae.load_kernels()
ae.fit()
ae.save_results()
