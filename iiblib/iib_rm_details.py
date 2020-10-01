class RmModel(object): # TODO maybe a new file

    _data_attrs = ["arches", "id", "request_type", "state", "state_reason", "state_history"]
    _kwarttrs = ["binary_image", "binary_image_resolved", "bundles", "bundle_mapping", "from_index", "from_index_resolved", "index_image", "organization", "removed-operators"]

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["arches"],#
            data["id"],#
            data["request_type"],
            data["state"],
            data["state_reason"],
            data["state_history"],
            data["binary_image"], #
            data["binary_image_resolved"],
            data["bundles"],
            data["bundle_mapping"],
            data["from_index"],#
            data["from_index_resolved"],
            data["index_image"],
            data["organization"],
            data["removed_operators"],
        )
