from os.path import join as pjoin
import pathlib
import numpy as np
import amico

amico.set_verbose(2)
print('\033[92m' + f'Running AMICO v{amico.__version__}' + '\033[0m')
sub = 'sandi'
bval = 'dwi_eddy_corr.bval'
bvec = 'dwi_eddy_corr.bvec'
scheme = 'scheme.txt'
b_step = 100
dwi = 'dwi_preproc_B1corr.nii.gz'
mask = 'brain_mask.nii.gz'
b0_thr = 10
big_delta = 0.03907
small_delta = 0.02466
te = 0.080
regenerate = True
study_path = pjoin(pathlib.Path(__file__).parent.resolve())
out_path = pjoin(pathlib.Path(__file__).parent.resolve(), 'res_' + amico.__version__, sub)
amico.setup()
amico.util.sandi2scheme(bvalsFilename=pjoin(study_path, sub, bval), bvecsFilename=pjoin(study_path, sub, bvec), Delta_data=big_delta, smalldel_data=small_delta, TE_data=te, schemeFilename=pjoin(study_path, sub, scheme), bStep=b_step)
ae = amico.Evaluation(study_path=study_path, subject=sub, output_path=out_path)
ae.set_config('doDebiasSignal', False)
ae.set_config('doDirectionalAverage', True)
ae.set_config('doComputeRMSE', True)
ae.set_config('doComputeNRMSE', True)
ae.load_data(dwi_filename=dwi, scheme_filename=scheme, mask_filename=mask, b0_thr=b0_thr)
ae.set_model('SANDI')
d_is = 3.0e-3                               # Intra-soma diffusivity [mm^2/s]
Rs = np.linspace(1.0, 12.0, 6) * 1e-6       # Radii of the soma [meters]
d_in = np.linspace(0.25, 3.0, 4) * 1e-3     # Intra-neurite diffusivitie(s) [mm^2/s]
d_isos = np.linspace(0.25, 3.0, 5) * 1e-3   # Extra-cellular isotropic mean diffusivitie(s) [mm^2/s]
ae.model.set(d_is=d_is, Rs=Rs, d_in=d_in, d_isos=d_isos)
ae.generate_kernels(regenerate=regenerate)
ae.load_kernels()
ae.set_solver(lambda1=0, lambda2=0.75e-3)
ae.fit()
ae.save_results(save_dir_avg=True)
