#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#


from extract_utils.fixups_blob import blob_fixup, blob_fixups_user_type
from extract_utils.fixups_lib import (
    lib_fixups_user_type,
    lib_fixups,
)
from extract_utils.main import ExtractUtils, ExtractUtilsModule

namespace_imports = [
    'vendor/oneplus/sm8150-common',
    'device/oneplus/sm8150-common',
    'vendor/qcom/common/vendor/media/legacy',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/libgf_ud_hal.so'
    ): blob_fixup()
        .replace_needed('vendor.boot.verifiedbootstate', 'vendor.boot.fingerprintbstate'),
    (
        'vendor/lib64/hw/com.qti.chi.override.so'
    ): blob_fixup()
        .add_needed('libcamera_metadata_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'oneplus7t',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8150-common', module.vendor
    )
    utils.run()
